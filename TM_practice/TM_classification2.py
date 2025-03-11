male = [
    {'deep voice':True, 'strong': True, 'short': False, 'sings':False, 'kind':True, 'breasts':False},
    {'deep voice':False, 'strong': True, 'short': True, 'sings':True, 'kind':True, 'breasts':False},
    {'deep voice':True, 'strong': False, 'short': False, 'sings':False, 'kind':True, 'breasts':False},
    {'deep voice':True, 'strong': True, 'short': False, 'sings':False, 'kind':False, 'breasts':False}
]

def check_gender(observation, condition):
    for feature in observation:
        static_condition = True
        if feature in condition and observation[feature] == False:
            static_condition = False
            break
    return static_condition
male_1 = ['deep voice', 'breasts']
print(check_gender(male[0], male_1)) # Expected output is False because male[0] has deep voice = True && Breasts = False
male_2 = ['deep voice', 'strong']
print(check_gender(male[0], male_2)) # Expected output is True because male[0] has deep voice && strong set to True
print(check_gender(male[1], male_2)) # Expected output is False because male[1] has deep voice = False && strong set to True
print(check_gender(male[2], male_2)) # Expected output is False because male[2] has deep voice = True && strong set to False
print(check_gender(male[3], male_2)) # Expected output is True because male[3] has deep voice && strong set to True




