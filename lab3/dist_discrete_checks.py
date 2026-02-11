from random import random
from random import choice

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
    pre_sample = bernoulli_sample(p, n)

    return sum(pre_sample)

def binom_sample(n, p, num):
    res = []

    for i in range(num):
        res.append(binom_once(n, p))

    return res

def geom_once(p):
    k = 1
    while True:
        res = bernoulli_once(p)
        if res:
            return k
        else:
            k += 1

def geom_sample_2(p, num):
    res = []
    for i in range(num):
        k = 1
        while random() >= p:
            k += 1
        res.append(k)
    return res

def geom_sample(p, num):
    res = []

    for i in range(num):
        res.append(geom_once(p))

    return res

def neg_binom_once(r, p):
    k = 1
    sample_counter = 0

    while True:
        res = bernoulli_once(p)
        if res:
            sample_counter += 1
            if sample_counter == r:
                return k
        else:
            k += 1

def neg_binom_once_opt(r, p):
    sample = geom_sample(p, r)

    return sum(sample)

def neg_binom_sample(r, p, num):
    res = []

    for i in range(num):
        res.append(neg_binom_once(r, p))

    return res

def neg_binom_sample_opt(r, p, num):
    res = []

    for i in range(num):
        res.append(neg_binom_once_opt(r, p))

    return res

def mult_geom_once(n, k):
    throw_counter = 0
    counter = 0
    choises = [i+1 for i in range(6)]

    while True:
        if counter >= n:
            return throw_counter

        res = choice(choises)

        counter += res
        throw_counter += 1

def mult_geom_sample(n, k, num):
    res = []

    for i in range(num):
        res.append(mult_geom_once(n, k))

    return res

