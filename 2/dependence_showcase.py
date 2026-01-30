import numpy as np
import matplotlib.pyplot as plt

n = 10_000

sample = np.random.randn(n)

x = sample
y = (sample*2) + 5

plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=5, alpha=0.5)
plt.grid(True)
plt.tight_layout()
plt.show()