import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_cylinder_by_lines():
    """
    Generates a cylinder by rotating a vertical line around the z-axis.
    The original line is fixed at (x=2, y=2) and extends along the z-axis.
    """
    z_vals = np.linspace(0, 5, 50)
    # Line generator at fixed x=2, y=2
    generator = np.array([2 * np.ones_like(z_vals), 2 * np.ones_like(z_vals), z_vals])

    # Rotation angles from 0 to 2π
    angles = np.linspace(0, 2 * np.pi, 50)

    x_cyl, y_cyl, z_cyl = [], [], []
    for theta in angles:
        # Rotation matrix around z-axis
        R = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta),  np.cos(theta), 0],
            [0,              0,             1]
        ])
        # Apply rotation to generator line
        rotated = R @ generator
        x_cyl.append(rotated[0])
        y_cyl.append(rotated[1])
        z_cyl.append(rotated[2])

    return np.array(x_cyl), np.array(y_cyl), np.array(z_cyl)

def generate_cone_by_lines():
    """
    Generates a cone by rotating an oblique line around the z-axis.
    The line passes through (0,0,2) with direction vector (0,2,-2).
    """
    k_vals = np.linspace(0, 1, 50)
    # Line generator points: (0, 2k, -2k + 2)
    generator = np.array([0 * k_vals, 2 * k_vals, 2 - 2 * k_vals])

    angles = np.linspace(0, 2 * np.pi, 50)

    x_cone, y_cone, z_cone = [], [], []
    for theta in angles:
        # Rotation matrix around z-axis
        R = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta),  np.cos(theta), 0],
            [0,              0,             1]
        ])
        # Rotate generator line around z-axis
        rotated = R @ generator
        x_cone.append(rotated[0])
        y_cone.append(rotated[1])
        z_cone.append(rotated[2])

    return np.array(x_cone), np.array(y_cone), np.array(z_cone)

# Generate data for the cylinder and cone
x_cyl, y_cyl, z_cyl = generate_cylinder_by_lines()
x_cone, y_cone, z_cone = generate_cone_by_lines()

# Plot the surfaces
fig = plt.figure(figsize=(12, 6))

# Plot cylinder
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x_cyl, y_cyl, z_cyl, color='blue', alpha=0.6)
ax1.set_title('Cylinder generated by rotating a vertical line')
ax1.set_xlabel('X'); ax1.set_ylabel('Y'); ax1.set_zlabel('Z')

# Plot cone
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x_cone, y_cone, z_cone, color='green', alpha=0.6)
ax2.set_title('Cone generated by rotating an oblique line')
ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('Z')

plt.tight_layout()
plt.show()
plt.savefig('cone_cylinder.png', dpi=300)
