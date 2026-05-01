import numpy as np

def cast(x):
    return np.array(x)

def transpose(x):
    return np.transpose(x)

def shapes(x):
    return (x.shape[0], x.shape[1])

def det(x):
    return np.linalg.det(x)

def inv(x):
    return np.linalg.inv(x)

def dot(x, v):
    return np.dot(x, v)

# Pseudo-inverse - for regression
def pinv(x):
    return np.linalg.pinv(x)