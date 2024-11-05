# exercise_9_distance_points.py

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = 1, 2
x2, y2 = 4, 6
print(f"The distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance(x1, y1, x2, y2):.2f}")
