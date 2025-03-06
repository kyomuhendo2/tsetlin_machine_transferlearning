# car features
cars = [
    {'Four Wheels':True, 'Transports People':True, 'Wings':False, 'Yellow':False, 'Blue':True},
    {'Four Wheels':True, 'Transports People':True, 'Wings':False, 'Yellow':True, 'Blue':False},
    {'Four Wheels':True, 'Transports People':True, 'Wings':False, 'Yellow':False, 'Blue':True}
]

# using AND and NOT to evaluate whether the condition is true or false
def check_condition(observation, condition):
    true_condition = True
    for feature in observation:
        if feature in condition and observation[feature] == False:
            true_condition = False
            break
        if 'NOT ' + feature in condition and observation[feature] == True:
            true_condition = False
            break
    return true_condition  
example_car = ['Four Wheels', 'Transports People','NOT Wings']
print(check_condition(cars[0], example_car))

