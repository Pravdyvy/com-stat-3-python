import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3*x - 5

def g(x):
    return x**2 - 5*x - 3

x = np.linspace(-10, 10, 400)

y1 = f(x)
y2 = g(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label=r"$f(x) = x^2 - 3x - 5$", color="blue")
plt.plot(x, y2, label="g(x) = x^2 - 5x - 3", color="green")

plt.axhline(0, color="red", linestyle=":", label="y = 0")

plt.title("Plot of the two quadratic functions")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid(True)
plt.legend()

plt.show()