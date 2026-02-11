import random

def rand_nat():
    num = random.random()

    if num == 0:
        return 1
    else:
        (1 / num) // 1