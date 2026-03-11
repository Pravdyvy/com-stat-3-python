import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3*x - 5

def g(x):
    return x**2 - 5*x - 3

x = np.linspace(-10, 10, 400)

fig, axes = plt.subplots(1, 2, figsize=(16, 5))

axes[0].plot(x, f(x), color="blue", label=r"$f(x) = x^2 - 3x - 5$")
axes[0].axhline(0, color="red", linestyle="--", label="y = 0")
axes[0].set_title("Function f(x)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].grid(True)
axes[0].legend()

axes[1].plot(x, g(x), color="green", label=r"$g(x) = x^2 - 5x - 3$")
axes[1].axhline(0, color="red", linestyle="--", label="y = 0")
axes[1].set_title("Function g(x)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()

plt.show()