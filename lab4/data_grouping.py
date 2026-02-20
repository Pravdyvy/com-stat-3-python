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
# returns list of pairs (number, its absolute frequency)
def grouped_sample(x):
    return [[i, absolute_freq(x, i)] for i in x]

# x - sorted sample of discrete distribution
# returns grouped mean of x
def grouped_mean(x):
    return 0

# x - sorted sample of discrete distribution
# returns grouped variance of x
def grouped_variance(x):
    return 0