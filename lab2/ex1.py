# mode [1,2,4,3,4,4,5,6,2]

import random

def sample_weighted_dice(num):
    results = []

    for i in range(0, num):
        res = random.choice([1,2,3,4,5,6])

        if res != 6:
            res = random.choice([1,2,3,4,5,6])
        
        results.append(res)

    return results

def mode(seq):
    mode = None
    max_count = 0

    for x in seq:
        count = 0
        for y in seq:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            mode = x

    return mode