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

# returns multiple samples of `sampler`
# number of samples is k, length is n
def multi_sample(k,n, sampler):
    return []

# executes statistic stat on each sample from `multi_sample`
def multi_sample_statistic(k,n, sampler, stat):
    return []

def prob_limit(stat, val, eps):
    return abs(stat - val) < eps

def prob_criterion(seq, val, eps):
    [prob_limit(x, val, eps) for x in seq].count(1) / len(seq)

# executes criterion for each statistic on each sample from `multi_sample`
def multi_sample_criterion(k,n, sampler, stat, criterion):
    return []