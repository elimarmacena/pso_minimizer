from entities.swarm import Swarm
import common.constants as const

def main():
    for i in range(NUM_EXECUTIONS):
        # First we will performe a iteration on every population size
        # and then move to the next max iteration
        for iteration_size in const.ITERATION_NUM:
            for population in const.POPULATION_SIZE:
                swarm_keeper = Swarm(population)
                iteration_controller = 0
                swarm_file = open(f'./outputs/best_particles_population{population}_iteration{iteration_size}_execution{i}.csv','w')
                while (iteration_controller < iteration_size):
                    swarm_keeper.set_best_particle()
                    line_writer = f'{iteration_controller};{swarm_keeper.get_best_particle()}\n'
                    swarm_file.write(line_writer)
                    swarm_keeper.update_population_location(iteration_controller,iteration_size)
                    iteration_controller += 1
            # end FOR population
            swarm_file.close()
        # end FOR iteration_size
    # end FOR i

main()