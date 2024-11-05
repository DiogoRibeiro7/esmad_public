# exercise_10_sum_of_squares.py

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

n = 5
print(f"The sum of squares up to {n} is: {sum_of_squares(n)}")
