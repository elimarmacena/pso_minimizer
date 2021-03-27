import common.constants as const
from random import random
from random import seed

seed(const.USED_SEED)
# lambda function to create positive or negative value
f_positive_negative= lambda x: x < 0.5 and 1 or -1
'''
    function used to create random location in a bidimentional plane
    @RETURN: list of floats
'''
def create_initial_location():    
    list_location = []
    # our case, the min and max of location are the negation of each one, the use of -1 or 1 is enough
    list_location.append(random() * const.MAX_POS * f_positive_negative(random())) 
    list_location.append(random() * const.MAX_POS * f_positive_negative(random()))
    return list_location

def create_initial_speed():
    initial_speed = random() * const.MAX_SPEED * f_positive_negative(random())
    return initial_speed
