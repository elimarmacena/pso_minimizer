import common.constants as consts
class Particle:
    def __init__(self,position, speed_x,speed_y):
        self.current_position = position # list as representation
        self.speed_x = speed_x # float as particle speed
        self.speed_y = speed_y # float as particle speed
        self.best_location = [self.current_position[0],self.current_position[1],self.calc_fitness()] # X, Y, fitness
    
    def get_current_position(self):
        return self.current_position
    def get_speed_x(self):
        return self.speed_x
    def get_speed_y(self):
        return self.speed_y
    def get_best_location(self):
        return self.best_location
    def get_x(self):
        return self.current_position[0]
    def get_y(self):
        return self.current_position[1]
    
    '''
        Function used to update all information about the particle if the update creates a better fitness
        returns True, otherwise, false 
        @Return: boolean
    '''
    def update_particle(self,w_value,best_particle):
        # x updates
        self.speed_update(w_value, best_particle, True)
        self.location_update(True)
        # y updates
        self.speed_update(w_value, best_particle, False)
        self.location_update(False)
        
        # checking if the new information is the best location that this particle has been
        new_fitness = self.calc_fitness()
        if self.best_location[2] > new_fitness:
            self.best_location[0] = self.current_position[0]
            self.best_location[1] = self.current_position[1]
            self.best_location[2] = new_fitness
            return True
        else:
            return False

    '''
        Function used to calculate the fitness, in the current problem, the value is calculate using the
        eggholder function. The lower value is better.
        -(y + 47)sin( sqrt( module( (x/2) + (y+47) ) ) ) - x * sin( sqrt( module( x - ( y+ 47 ) ) ) )
        @Return: float value
    '''
    def calc_fitness(self):
        x = self.current_position[0]
        y = self.current_position[1]
        y_operation = y + 47

        sin1_content = abs( (x/2) + y_operation)
        sin1 = sin(sqrt(sin1_content))
        term1 = -(y_operation) * sin1
        
        sin2_content = abs(x - y_operation)
        sin2 = sin(sqrt(sin2_content))
        term2 = -x * sin2
        final_result = term1 + term2
        return final_result

    '''
        Function used to update the particle speed, the function follows the formule
        W * Vi(t) + c1 * random * (LocalBest - xi(t)) + c2 * random * (GlobalBest -xi(t))
        @Param:
            w_value: float value used to replace W in the formule
            best_particle: Particle with the best global results (best fitness)
            is_x: boolean used as flag to calculate the speed update in the X or Y axis
    '''
    def speed_update(self, w_value:float, best_particle:Particle, is_x:bool):
        # As a bidimencional space, the use of IF ElSE is enough
        new_speed = 0.0
        if is_x:
            local_calc = random() * (self.best_location[0] - self.current_position[0])
            global_calc = random() * (best_particle.get_x() - self.current_position[0])
            new_speed = (w_value * self.speed_x) + (consts.C1 * local_calc) + (consts.C2 * global_calc)
        # end IF is_x
        else:
            local_calc = random() * (self.best_location[1] - self.current_position[1])
            global_calc = random() * (best_particle.get_y() - self.current_position[1])
            new_speed = (w_value * self.speed_y) + (consts.C1 * local_calc) + (consts.C2 * global_calc)
        # end ELSE
        return new_speed
    
    '''
        Function used to update the current location, to used this function is necessary perform a speed
        update before to follow the swarm logic.
    '''
    def location_update(self,is_x):
        if is_x:
            self.current_position[0] += self.speed_x
        else:
            self.current_position[1] += self.speed_y
