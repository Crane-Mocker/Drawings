import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import laplace

epsilon = 4
sensitivity = 5
b = sensitivity / epsilon 


f_D = 100  # Assume sum of weights in D
f_D_prime = f_D - 5

# Generate Laplace noise
x = np.linspace(-200, 200, 1000)
laplace_D = laplace.pdf(x, loc=f_D, scale=b)
laplace_D_prime = laplace.pdf(x, loc=f_D_prime, scale=b)

plt.figure(figsize=(8, 5))
plt.plot(x, laplace_D, label=fr'$M(D) = f(D) + \mathrm{{Lap}}({b})$', color='blue')
plt.plot(x, laplace_D_prime, label=fr"$M(D') = f(D') + \mathrm{{Lap}}({b})$", color='red')

plt.axvline(f_D, color='blue', linestyle='dashed', alpha=0.5, label=r'$f(D)$')
plt.axvline(f_D_prime, color='red', linestyle='dashed', alpha=0.5, label=r"$f(D')$")

# Annotating the difference
plt.annotate(r"$|f(D) - f(D')| = 5$", xy=((f_D + f_D_prime) / 2, 0.0035),
             xytext=(0, 10), textcoords='offset points', ha='center', fontsize=12,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

plt.xlabel("Output value")
plt.ylabel("Probability Density")
plt.title("Laplace Mechanism for Neighboring Datasets")

# Remove x-axis numbers
plt.xticks([])

plt.legend()
plt.grid(True)
plt.show()
