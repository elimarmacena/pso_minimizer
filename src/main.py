from entities.swarm import Swarm
import common.constants as const

def main():
    swarm_keeper = Swarm(2)
    print(swarm_keeper.calc_fitness([512,404.2319]))
    #for population in const.POPULATION_SIZE:
    #    swarm_keeper = Swarm(population)
    #    print(swarm_keeper)
    # End FOR population

main()