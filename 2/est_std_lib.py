def mean(x):
    sum = 0
    for i in x:
        sum += i
    return sum/len(x)

def median(x):
    sorted_x = sorted(x)
    length_x = len(x)
    if length_x % 2 == 1:
        median = sorted_x[length_x // 2]
    else:
        median = (sorted_x[length_x // 2 - 1] + sorted_x[length_x // 2])/2 
    return median

def variance(x):
    mean_x = mean(x)
    x_squared = [(i - mean_x) ** 2 for i in x]
    return sum(x_squared)/len(x)

def variance_wrong(x):
    mean_x = mean(x)
    x_squared = [i ** 2 for i in x]
    meax_x_squared = mean(x_squared)
    return (meax_x_squared - mean_x**2)/len(x)