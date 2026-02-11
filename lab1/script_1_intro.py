import numpy as np
import matplotlib.pyplot as plt

# Parameters
mean = 10
std = 100
n_samples = 10000

# Generate dataset
data = np.random.normal(loc=mean, scale=std, size=n_samples)

# Define PDF function for normal distribution
def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Create x values for PDF
x = np.linspace(data.min(), data.max(), 1000)
pdf = normal_pdf(x, mean, std)

# Plot
plt.figure(figsize=(8, 5))
plt.hist(data, bins=40, density=True, alpha=0.6, label="Dataset (histogram)")
plt.plot(x, pdf, 'r', label="Normal PDF")

plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Normal Distribution PDF (μ=10, σ=100)")
plt.legend()
plt.tight_layout()
plt.show()