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

# Plant features
maize = [
    {'color green': True, 'grown for food': True, 'tall stalk': True, 'dicot seed': True, 'tap root': False, 'ugandan': False},
    {'color green': True, 'grown for food': True, 'tall stalk': True, 'dicot seed': False, 'tap root': False, 'ugandan': True},
    {'color green': True, 'grown for food': True, 'tall stalk': True, 'dicot seed': False, 'tap root': False, 'ugandan': False}
]

def check_maize(observe, physical_features):
    t_condition = True  # Assume the condition is True at first
    for feature in physical_features:
        if feature in observe:
            if observe[feature] == False:  # If it's False in the observation, set t_condition to False
                t_condition = False
                break  # Exit the loop immediately as the condition is already False
        else:
            # If the feature is not in the observation at all, set t_condition to False
            t_condition = False
            break  # Exit the loop immediately since the feature is missing
    return t_condition

maize1 = ['color green', 'grown for food', 'ugandan']
print('maize1 is: ', check_maize(maize[0], maize1))  # Expected: False, since 'ugandan' is False in maize[0]

maize2 = ['color green', 'grown for food', 'dicot seed']
print('maize2 is: ', check_maize(maize[0], maize2))  # Expected: True, as all conditions are True for maize[0]

maize3 = ['color green', 'grown for food', 'tall stalk']
print('maize3 is: ', check_maize(maize[0], maize3))  # Expected: True, as all conditions are True for maize[0]


# Lake features
lake = [
    {'is wide': True, 'is deep': True, 'flowing' : False, 'cloudy': False, 'clear': False},
    {'is wide': True, 'is deep': True, 'flowing' : True, 'cloudy': False, 'clear': True},
    {'is wide': True, 'is deep': True, 'flowing' : True, 'cloudy': False, 'clear': True},
]

def check_lake(x, y):
    tru_condition = True
    for m in y:
        if m in x:
            if x[m] == False:
                tru_condition = False
                break
        else:
            tru_condition = False
            break
    return tru_condition
lake1 = ('is wide','is deep','flowing','cloudy')
print('lake 1 is : ', check_lake(lake[0], lake1))
lake2 = ('is wide','is deep','flowing','clear')
print('lake 2 is : ', check_lake(lake[1], lake2))

