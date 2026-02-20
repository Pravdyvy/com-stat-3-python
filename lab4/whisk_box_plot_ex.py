import numpy as np
import matplotlib.pyplot as plt

def boxplot1():
    sample1 = [-10,-9,1,1,8,9,9,9,9,12,13,14,15,15,15,15,20,21,22,27,28,45,70]

    np_sample1 = np.array(sample1)

    plt.boxplot(np_sample1)
    plt.show()

def boxplot2():
    np_sample2 = np.random.normal(loc=0, scale=1, size=10000)

    plt.boxplot(np_sample2)
    plt.show()

boxplot2()