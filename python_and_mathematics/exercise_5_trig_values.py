# exercise_5_trig_values.py

import math

def trig_values():
    angles = range(0, 361, 30)
    for angle in angles:
        rad = math.radians(angle)
        print(f"Angle: {angle}°, Sine: {math.sin(rad):.2f}, Cosine: {math.cos(rad):.2f}")

trig_values()
