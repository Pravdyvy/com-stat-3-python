from math import floor, ceil

def sort_seq(x):
    x.sort()

def variance(x):
    return max(x) - min(x)

# x - sorted array
# returns empiric quantile of level p
#
# For p = 0 - returns the least value
# For p = 1 - returns the biggest value
def quantile(x,p):
    if p == 0:
        return min(x)
    if p == 1:
        return max(x)
    
    if floor(len(x)*p) == 0:
        left_sat_id = 0
    else:
        left_sat_id = floor(len(x)*p) - 1
    
    left_half_quan = x[left_sat_id]
    right_half_quan = x[ceil(len(x)*p) - 1]

    return (left_half_quan + right_half_quan)/2

# x - sorted array
# returns inter quartile variance
def iqr(x):
    q1 = quantile(x, 0.25)
    q3 = quantile(x, 0.75)
    return q3 - q1

# x - sorted array
# returns vector of statistics, necessary for whisker box plot
def whisker_box_stats(x):
    q1 = quantile(x, 0.25)
    q2 = quantile(x, 0.5)
    q3 = quantile(x, 0.75)
    
    iqr_value = iqr(x)
    
    lower_whisker = q1 - 1.5 * iqr_value
    upper_whisker = q3 + 1.5 * iqr_value
    
    return [quantile(x,0), lower_whisker, q1, q2, q3, upper_whisker, quantile(x,1)]
