import numpy as np

# дані
sample = np.array([5.1, 4.9, 5.0, 5.2, 5.1])
sigma = 0.1  # відоме стандартне відхилення
n = len(sample)

# середнє
x_bar = np.mean(sample)

# Quantile[NormalDistribution[0, 1], 0.975]
z = 1.96

# межі інтервалу
margin = z * sigma / np.sqrt(n)
ci_lower = x_bar - margin
ci_upper = x_bar + margin

print(f"95% довірчий інтервал: [{ci_lower:.4f}, {ci_upper:.4f}]")