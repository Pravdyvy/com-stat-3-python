from random import random

def uniform_once(a, b):
    return (random() * (b-a)) + a

def uniform_sample(a, b, num):
    res = []

    for i in range(num):
        res.append(uniform_once(a, b))

    return res

def mean(x):
    sum = 0
    for i in x:
        sum += i
    return sum/len(x)

def variance(x):
    mean_x = mean(x)
    x_squared = [i ** 2 for i in x]
    meax_x_squared = mean(x_squared)
    return meax_x_squared - mean_x**2

# Returns sequence [1, ..., n]
def enumeration(n):
    return list(range(1,n+1))

# Returns running statistic `stat` on sample x
# x - sample of some distribution
# stat(x) - function, which takes one arg(seq)
def running_statistic(x, stat):
    res = []

    for i in range(1, len(x)+1):
        res.append(stat(x[:i]))

    return res

# Returns estimate of left boundary of uniform[left, right]
# using method of moments `left = mean - sqrt(3*variance)`
def omm_stat_uniform_left(x):
    return mean(x) - (3 * variance(x)) ** 0.5