from entities.particle import Particle
from math import sqrt,sin
import common.utils as util

class Swarm:
    def __init__(self,population_size):
        self.population_control = [None] * population_size
        self.best_partitle = None
        self.__create_initial_population()
        
    
    '''
        Function used to calculate the fitness, in the current problem, the value is calculate using the
        eggholder function. The lower value is better.
        -(y + 47)sin( sqrt( module( (x/2) + (y+47) ) ) ) - x * sin( sqrt( module( x - ( y+ 47 ) ) ) )
        @Return: float value
    '''
    def calc_fitness(self,location):
        x = location[0]
        y = location[1]
        y_operation = y + 47

        sin1_content = abs( (x/2) + y_operation)
        sin1 = sin(sqrt(sin1_content))
        term1 = -(y_operation) * sin1
        
        sin2_content = abs(x - y_operation)
        sin2 = sin(sqrt(sin2_content))
        term2 = -x * sin2
        final_result = term1 + term2
        return final_result


    def __create_initial_population(self):
        counter  = 0;
        initial_speed = util.create_initial_speed() #initial speed used to the whole swarm
        while counter < len(self.population_control):
            new_particle = Particle(util.create_initial_location(), initial_speed)
            self.population_control[counter] = new_particle
            counter += 1
        # end WHILE counter