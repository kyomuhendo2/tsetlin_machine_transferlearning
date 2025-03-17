# Importing necessary libraries
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_iput
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from PIL import Image

# Image Preprocessing
def image_preprocessor(image_path, target_size=()):

    # Loading the image
    img = Image.open(image_path)
    
    # Converting to RGB since VGG19 expects 3 channels
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Resizing the input to VGG19 input size
    img = img.resize(target_size)
    
    # Converting to array
    img_array = np.array(img)

    # Expanding dimensions to create a batch
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocessing for VGG19
    img_array = preprocess_iput(img_array)
    return img_array

# Defining the VGG19 feature extractor function
def vgg19_feature_extractor():

    # Using Imagenet weights and ignoring the last layer
    base_model = VGG19(weights='imagenet', include_top=False)
    feature_extractor = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)
    return feature_extractor

# Extracting features from a single image
def feature_extraction(image_path, model):

    # Image preprocessing
    processed_img = image_preprocessor(image_path)

    # Extract the features
    features  = model.predict(processed_img)
    
    # Flatten features
    flat_features = features.flatten()
    return flat_features

# Extracting features from all the images
def process_dataset(data_dir, output_file='extracted_features.npy'):

    # Creating a feature extractor
    feature_extractor = vgg19_feature_extractor()
    features_list = []
    labels = []

    for class_name in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, class_name)
        if os.path.isdir(class_dir):
            for image_name in os.listdir(class_dir):
                image_path = os.path.join(class_dir, image_name)
                try:

                    # Extracting features
                    features = feature_extraction(image_path, feature_extractor)
                    features_list.append(features)
                    labels.append(class_name)

                    print(f'processed: {image_path}')
                except Exception as e:
                    print(f'Error processing {image_path} : {str(e)}')

    #Converting to numpy arrays
    features_array = np.array(features_list)
    labels_array = np.array(labels)

    # Saving to numpy arrays
    np.save(output_file, features_array)
    np.save('labels.npy', labels_array)
    return features_array

# Example
if __name__ == '__main__':
    # Dataset directory
    data_directory = 'path/to/your/mri/dataset'

    # Processing the dataset
    features, labels = process_dataset(data_directory)
    print(f'Extracted features shape : {features.shape}')
    print(f'Number of samples: {len(labels)}')