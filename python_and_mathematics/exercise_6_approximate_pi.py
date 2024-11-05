# exercise_6_approximate_pi.py

def approximate_pi(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i / (2 * i + 1)
    return 4 * pi

n = 100000
print(f"Approximation of pi with {n} terms: {approximate_pi(n)}")
