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
    return [sampler(n) for i in range(k)]

# executes statistic stat on each sample from `multi_sample`
def multi_sample_statistic(k,n, sampler, stat):
    return [stat(sample) for sample in multi_sample(k,n,sampler)]

def prob_limit(stat, val, eps):
    if abs(stat - val) < eps:
        return 1
    else:
        return 0

def prob_criterion(seq, val, eps):
    return [prob_limit(x, val, eps) for x in seq].count(1) / len(seq)

def prob_criterion_u_mean(seq):
    return prob_criterion(seq, 3, 0.1)

def prob_criterion_u_var(seq):
    return prob_criterion(seq, 1/3, 0.1)

def uniform_sampler_u(num):
    return uniform_sample(2,4,num)

# executes criterion for each statistic on each sample from `multi_sample`
def multi_sample_criterion(k,n, sampler, stat, criterion):
    return []

from lab5.running_statistics import running_statistic

x = multi_sample_statistic(100,100,uniform_sampler_u,mean)
y = running_statistic(x, prob_criterion_u_mean)

x_coor = list(range(1,101))

import matplotlib.pyplot as plt

plt.plot(x_coor, y)
plt.show()

