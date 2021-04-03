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

'''
    Defines random value to be used as initial speed
'''
def create_initial_speed():
    initial_speed = random() * const.MAX_SPEED * f_positive_negative(random())
    return initial_speed

'''
    Function used to create a dict of means based on the code execution.
'''
def create_mean_executions(dict_bests):
    dict_means = {}
    for population in const.POPULATION_SIZE:
        iteration_history = {}
        for total_iteration in const.ITERATION_NUM:
            local_history = {}
            for i in range(total_iteration):
                iteration_num_acc = 0
                for execution in range(const.NUM_EXECUTIONS):
                    iteration_num_acc += dict_bests[execution][total_iteration][population][i]
                # end FOR execution
                local_history[i] = iteration_num_acc / const.NUM_EXECUTIONS
            # end FOR i
            iteration_history[total_iteration] = local_history
        # end FOR total_iteration
        dict_means[population] = iteration_history
    # end FOR population
    return dict_means

    return 0
