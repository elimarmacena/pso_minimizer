import statistics
from entities.swarm import Swarm
import common.constants as const
import common.utils as utils



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
                while (iteration_controller < iteration_size):
                    swarm_keeper.set_best_particle()
                    line_writer = f'{iteration_controller};{swarm_keeper.get_best_particle()}\n'
                    local_history[iteration_controller] = swarm_keeper.get_best_particle().calc_fitness()
                    swarm_keeper.update_population_location(iteration_controller,iteration_size)
                    iteration_controller += 1
                population_history[population] = local_history
            # end FOR population
            max_iteration_history[iteration_size] = population_history
        # end FOR iteration_size
        execution_history[i] = max_iteration_history
    # end FOR i
    utils.write_execution_tables(execution_history)
    mean_executions = utils.create_mean_executions(execution_history)
    utils.write_execution_file(mean_executions)   
main()