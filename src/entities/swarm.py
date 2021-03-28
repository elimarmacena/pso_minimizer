from entities.particle import Particle
from math import sqrt,sin
import common.utils as util

class Swarm:
    def __init__(self,population_size):
        self.population_control = [None] * population_size
        self.best_particle = None
        self.__create_initial_population()
        
    


    '''
        Function used to calculate the current W value
        @RETURN: float
    '''
    def get_w_value(self,current_iteration, max_iteration):
        w_fraction = (const.W_MAX - const.W_MIN) / max_iteration
        w_value = const.W_MAX - (current_iteration * w_fraction)
        return w_value

    def __create_initial_population(self):
        counter  = 0;
        initial_speed_x = util.create_initial_speed() #initial speed used to the whole swarm
        initial_speed_y = util.create_initial_speed() #initial speed used to the whole swarm
        while counter < len(self.population_control):
            new_particle = Particle(util.create_initial_location(), initial_speed_x,initial_speed_y)
            self.population_control[counter] = new_particle
            counter += 1
        # end WHILE counter