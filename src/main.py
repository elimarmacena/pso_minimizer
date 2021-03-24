from entities.swarm import Swarm
import common.constants as const

def main():
    for population in const.POPULATION_SIZE:
        swarm_keeper = Swarm(population)
        print(population)
    # End FOR population

main()