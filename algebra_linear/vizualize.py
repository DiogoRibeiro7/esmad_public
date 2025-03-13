import matplotlib.pyplot as plt
import numpy as np

# Visualização simples em 2D
fig, ax = plt.subplots()

# Vetores
v1 = np.array([2, 3])
v2 = np.array([1, -2])

ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid()
ax.legend()
plt.show()
