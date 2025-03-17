male = [
    {'deep voice':True, 'strong': True, 'short': False, 'sings':False, 'kind':True, 'breasts':False},
    {'deep voice':False, 'strong': True, 'short': True, 'sings':True, 'kind':True, 'breasts':False},
    {'deep voice':True, 'strong': False, 'short': False, 'sings':False, 'kind':True, 'breasts':False},
    {'deep voice':True, 'strong': True, 'short': False, 'sings':False, 'kind':False, 'breasts':False}
]

female = [
    {'deep voice':False, 'strong': True, 'short': False, 'sings':False, 'kind':True, 'breasts':True},
    {'deep voice':False, 'strong': True, 'short': True, 'sings':True, 'kind':True, 'breasts':True},
    {'deep voice':False, 'strong': False, 'short': True, 'sings':False, 'kind':True, 'breasts':True},
    {'deep voice':False, 'strong': True, 'short': False, 'sings':False, 'kind':False, 'breasts':True}
]

def check_gender(observation, condition):
    for feature in observation:
        static_condition = True
        if feature in condition and observation[feature] == False:
            static_condition = False
            break
    return static_condition



