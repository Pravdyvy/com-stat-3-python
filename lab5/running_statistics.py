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
    return []

# Returns running statistic `stat` on sample x
# x - sample of some distribution
# stat(x) - function, which takes one arg(seq)
def running_statistic(x, stat):
    return []