import common.constants as consts
class Particle:
    def __init__(self,position, speed):
        self.current_position = position # list as representation
        self.speed = speed # float as particle speed
        self.best_location = [None,None]
    
    def get_current_position(self):
        return self.current_position
    def get_speed(self):
        return self.speed
    def get_best_location(self):
        return self.best_location
    def get_x(self):
        return self.current_position[0]
    def get_y(self):
        return self.current_position[1]
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

    '''
        Function used to update the particle speed, the function follows the formule
        W * Vi(t) + c1 * random * (LocalBest - xi(t)) + c2 * random * (GlobalBest -xi(t))
    '''
    # GENERALIZAR PARA CALCULAR X E Y AO MESMO TEMPO
    def speed_update(self, w_value, best_particle):
        local_calc = random() * (self.best_location[0] - self.current_position[0])
        global_calc = random() * (best_particle.get_x() - self.current_position[0])
        new_speed = (w_value * self.speed) + (consts.C1 * local_calc) + (consts.C2 * global_calc)
        return new_speed
    
    #FAZER GENERALIZADA PRA X E Y
    def location_update(self):
        return 0
