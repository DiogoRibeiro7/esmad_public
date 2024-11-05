# exercise_4_quadratic_roots.py

import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return "Complex roots"

a, b, c = 1, -3, 2
print(f"The roots are: {quadratic_roots(a, b, c)}")
