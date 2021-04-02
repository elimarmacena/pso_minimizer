import copy
from entities.particle import Particle
from math import sqrt,sin
import common.utils as util
import common.constants as const

class Swarm:
    def __init__(self,population_size):
        self.population_control = [None] * population_size
        self.best_particle = None
        self.__create_initial_population()
        
    
    def get_population_control(self):
        return self.population_control
    def get_best_particle(self):
        return self.best_particle
    '''
        Performs a verification on each particle to find the best (lowest) fitness and set the particle to
        @best_particle
    '''
    def set_best_particle(self):
        current_best = self.best_particle
        current_best_fitness = current_best.calc_fitness()
        for current_particle in self.population_control:
            fitness_particle = current_particle.calc_fitness()
            if(current_best_fitness > fitness_particle):
                current_best = current_particle
                current_best_fitness = fitness_particle
            # end IF
        # end FOR current_particle
        # the copy is used to void erro when update a particle
        self.best_particle = copy.deepcopy(current_best)
    
    def update_population_location(self,current_iteration, max_iteration):
        w_value = self.get_w_value(current_iteration, max_iteration)
        for current_particle in self.population_control:
            current_particle.update_particle(w_value,self.best_particle)

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
        # set any particle as contructor best.
        self.best_particle = self.population_control[0]