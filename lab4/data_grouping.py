# x - sorted sample of discrete distribution
# n - number
# returns absolute frequence of n
def absolute_freq(x, n):
    return x.count(n)

# x - sorted sample of discrete distribution
# n - number
# returns relative frequence of n
def relative_freq(x, n):
    return absolute_freq(x, n)/len(x)

# x - sorted sample of discrete distribution
# returns dictionary (number, its absolute frequency)
def grouped_sample(x):
    sample_dict = dict()
    for i in x:
        sample_dict[i] = absolute_freq(x, i)
    return sample_dict

# x - sorted sample of discrete distribution
# returns grouped mean of x
def grouped_mean(x):
    grouped_x = grouped_sample(x)
    n = len(x)
    return sum(xi[0] * (xi[1]/n) for xi in grouped_x.items())

# x - sorted sample of discrete distribution
# returns grouped variance of x
def grouped_variance(x):
    mean = grouped_mean(x)
    grouped_x = grouped_sample(x)
    n = len(x)
    return sum((xi[1]/n)*(xi[0] - mean)**2 for xi in grouped_x.items())

# x - sorted sample of any distribution
# returns dictionary (number, its absolute frequency)
def grouped_sample_force(x, line_lambda):
    res = dict()

    for el_lambda in line_lambda:
        res[el_lambda] = []

    i = 0
    j = 0

    while i < len(x):
        if x[i] <= line_lambda[j]:
            res[line_lambda[j]].append(x[i])
        else:
            j += 1
        i += 1

    return res 