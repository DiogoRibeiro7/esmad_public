from scipy.optimize import brentq
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

LOWER_LIMIT = 0
UPPER_LIMIT = 0.8

# Define the function


def f(x):
    return (x**2 - 1) * np.exp(x**3 - 3*x)


def f(x):
    return np.exp(-3*x)

# Define the x range and calculate y
x = np.linspace(-4, 2, 500)
y = f(x)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = (x² - 1) * e^(x³ - 3x)', color='blue')

# Fill the area under the curve between x = -1 and x = 1
x_fill = np.linspace(LOWER_LIMIT, UPPER_LIMIT, 200)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5,
                 label=f'Area under curve ({LOWER_LIMIT} to {UPPER_LIMIT})')

# Add labels, legend, and grid
plt.title('Plot of y = (x² - 1) * e^(x³ - 3x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Integrate the function between -1 and 0
area, _ = quad(f, LOWER_LIMIT, UPPER_LIMIT)
print(area)
print(np.abs(area))


# Define the function for root-finding

def f_root(x):
    return f(x)


# Find the roots of the function within the domain [-3, 2]
root1 = brentq(f_root, -3, 0)
root2 = brentq(f_root, 0, 2)

print(root1, root2)

# Define the intervals for integration
intervals = [(-2, root1), (root1, root2), (root2, 2)]

# Calculate the total absolute area
total_absolute_area = sum(quad(lambda x: abs(f(x)), a, b)[0] for a, b in intervals)
print(total_absolute_area)
