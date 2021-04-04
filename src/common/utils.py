import statistics
import common.constants as const
from random import random
from random import seed
try:
    from matplotlib import pyplot
except ModuleNotFoundError:
    print('matplotlib was not fund. \nPlease, run: \n\t\'pip install matplotlib\' or \'pip3 install matplotlib\' \nto install the library')
    exit(1)

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

def write_execution_tables(execution_history):
    table_file = open('./outputs/executions_statisctic.csv','w')
    table_file.write('population;max_iterations;execution;best_fitness;mean;standard_deviation\n')
    for iterations in const.ITERATION_NUM:
        for population in const.POPULATION_SIZE:
            for execution in range(const.NUM_EXECUTIONS):
                best_fitness = min(execution_history[execution][iterations][population].values())
                mean_execution = sum(execution_history[execution][iterations][population].values())/iterations
                st_dev = statistics.stdev(execution_history[execution][iterations][population].values())
                line_writer = f'{population};{iterations};{execution};{best_fitness:.4f};{mean_execution:.4f};{st_dev:.4f}\n'
                table_file.write(line_writer)
            # end FOR execution
        # end FOR population
    # end FOR iterations
    table_file.close()

def write_execution_file(dict_execution):
    for population in const.POPULATION_SIZE:
        for iteration_size in const.ITERATION_NUM:
            execution_file = open(f'./outputs/executions_population{population}_iterationmax{iteration_size}.csv','w')
            execution_file.write('iteration;mean_execution\n')
            for i in range(iteration_size):
                line_writer = f'{i};{dict_execution[population][iteration_size][i]}\n'
                execution_file.write(line_writer)
            # end FOR i
            execution_file.close()
        # end FOR iteration_size
    # end FOR population

def plot_mean_executions(dict_mean):
    for population in const.POPULATION_SIZE:
        for iteration_num in const.ITERATION_NUM:
            axis_x = []
            axis_y = []
            for i in range(iteration_num):
                axis_x.append(i)
                axis_y.append(dict_mean[population][iteration_num][i])
            pyplot.plot(axis_x,axis_y,marker='o')
            pyplot.xlabel("Iteração")
            pyplot.ylabel("Média Fitness da I-ésima Iteração")
            pyplot.title(f'População {population}, Num. Iterações {iteration_num}')
            pyplot.show()
