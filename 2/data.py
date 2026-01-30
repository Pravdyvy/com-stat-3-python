import numpy as np
import math

def sample_norm_dist(mean, var, num):
    return np.random.normal(mean, math.sqrt(var), num)

def sample_chi_square(free_deg, num):
    return np.random.chisquare(free_deg, num)