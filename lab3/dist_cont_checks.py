from random import random

def uniform_once(a, b):
    return (random() * (b-a)) + a

def uniform_sample(a, b, num):
    res = []

    for i in range(num):
        res.append(uniform_once(a, b))

    return res