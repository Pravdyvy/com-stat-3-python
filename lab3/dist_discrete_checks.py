from random import random

def bernoulli_once(p):
    s = random()

    if s < p:
        return 1
    else:
        return 0

def bernoulli_sample(p, num):
    res = []

    for i in range(num):
        res.append(bernoulli_once(p))

    return res

def binom_once(n, p):
    return 0

def binom_sample(n, p, num):
    res = []

    for i in range(num):
        res.append(binom_once(n, p))

    return res

def geom_once(p):
    return 0

def geom_sample(p, num):
    res = []

    for i in range(num):
        res.append(geom_sample(p))

    return res

def neg_binom_once(r, p):
    return 0

def neg_binom_sample(r, p, num):
    res = []

    for i in range(num):
        res.append(neg_binom_once(r, p))

    return res

