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
    return 0

# x - sorted array
# returns inter quartile variance
def iqr(x):
    return 0

# x - sorted array
# returns vector of statistics, necessary for whisker box plot
def whisker_box_stats(x):
    return []
