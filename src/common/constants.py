USED_SEED = 21
NUM_EXECUTIONS = 10
POPULATION_SIZE = [50, 100]
ITERATION_NUM = [20, 50, 100]
MIN_POS = -512
MAX_POS = 512

# 15% of the min and max positition
MIN_SPEED = -77
MAX_SPEED = 77

'''
    The following values are proposed by Shi and Eberhart(1998), those values had presented good results in
    general.
    REF:Shi, Y., Eberhart, R.C. (1998) “A Modified Particle Swarm Optimizer”,
        In: IEEE World Congress on Computational Intelligence, Anchorage, Alaska, pp.69-73
'''
# Weighting const
W_MIN = 0.9
W_MAX = 0.4

# Const of speed update
C1 = 2
C2 = 2