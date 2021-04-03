import statistics
from entities.swarm import Swarm
import common.constants as const
import common.utils as utils

def write_execution_file(dict_execution):
    for population in const.POPULATION_SIZE:
        for iteration_size in const.ITERATION_NUM:
            print(f'Standard Deviation [Population - {population} Iteration - {iteration_size}]: {statistics.stdev(dict_execution[population][iteration_size]):.4f}')
            execution_file = open(f'./outputs/executions_population{population}_iterationmax{iteration_size}.csv','w')
            execution_file.write('iteration;mean_execution\n')
            for i in range(iteration_size):
                line_writer = f'{i};{dict_execution[population][iteration_size][i]}\n'
                execution_file.write(line_writer)
            # end FOR i
            execution_file.close()
        # end FOR iteration_size
    # end FOR population

def main():
    execution_history = {}
    for i in range(const.NUM_EXECUTIONS):
        print(f'EXECUTION {i} - SWARM')
        # First we will performe a iteration on every population size
        # and then move to the next max iteration
        max_iteration_history = {}
        for iteration_size in const.ITERATION_NUM:
            population_history = {}
            for population in const.POPULATION_SIZE:
                swarm_keeper = Swarm(population)
                iteration_controller = 0
                local_history = {}
                swarm_file = open(f'./outputs/best_particles_population{population}_iteration{iteration_size}_execution{i}.csv','w')
                swarm_file.write('iteration;fitness;location_x;location_y\n')
                while (iteration_controller < iteration_size):
                    swarm_keeper.set_best_particle()
                    line_writer = f'{iteration_controller};{swarm_keeper.get_best_particle()}\n'
                    swarm_file.write(line_writer)
                    local_history[iteration_controller] = swarm_keeper.get_best_particle().calc_fitness()
                    swarm_keeper.update_population_location(iteration_controller,iteration_size)
                    iteration_controller += 1
                population_history[population] = local_history
            # end FOR population
            swarm_file.close()
            max_iteration_history[iteration_size] = population_history
        # end FOR iteration_size
        execution_history[i] = max_iteration_history
    # end FOR i
    mean_executions = utils.create_mean_executions(execution_history)
    write_execution_file(mean_executions)   
main()