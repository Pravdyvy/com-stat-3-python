import numpy as np
import matplotlib.pyplot as plt

def pdf(sample, num_bins):
    []

def cdf(sample, num_bins):
    []

def draw_cdf(samples, num_bins):
    x, y = cdf(samples, num_bins)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='.', linestyle='-', label="Empirical CDF")

    plt.title("Empirical Cumulative Distribution Function (CDF)")
    plt.xlabel("x")
    plt.ylabel("F(x)")

    plt.grid(True)
    plt.legend()

    plt.show()

def draw_pdf(samples, num_bins):
    density, bins = pdf(samples, num_bins)

    bin_centers = (bins[:-1] + bins[1:]) / 2

    plt.figure(figsize=(8,5))
    plt.plot(bin_centers, density, marker='o', linestyle='--', label="Estimated PDF")

    plt.title("Estimated Probability Density Function (PDF)")
    plt.xlabel("x")
    plt.ylabel("Probability Density")

    plt.grid(True)
    plt.legend()

    plt.show()

# samples = np.random.normal(loc=0, scale=1, size=1000)

# draw_pdf(samples, 30)

# draw_cdf(samples, 30)


