from scipy.stats import norm,kstwo
import numpy as np

n = 20
alpha = 0.05

mu = n * (n + 1) / 4
sigma = np.sqrt(n * (n + 1) * (2*n + 1) / 24)

z = norm.ppf(1 - alpha)
q = mu + z * sigma

# Wilcoxon
print(q)

n = 50          
alpha = 0.05    

q = kstwo.ppf(1 - alpha, n)

# Kolmogorov-Smirnov
print(q)