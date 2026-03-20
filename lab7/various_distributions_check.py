from numpy.random import standard_normal, standard_t, f, chisquare
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

rng = random.default_rng()

def pdf(samples):
    counts, bins = np.histogram(samples, bins=30, density=True)

    bin_centers = (bins[:-1] + bins[1:]) / 2

    plt.plot(bin_centers, counts, label="Estimated PDF")
    plt.legend()
    plt.show()

def cdf(samples):
    sorted_samples = np.sort(samples)
    cdf = np.arange(1, len(samples)+1) / len(samples)

    plt.plot(sorted_samples, cdf, label="Empirical CDF")
    plt.legend()
    plt.show()