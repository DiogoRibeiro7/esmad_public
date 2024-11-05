# exercise_1_factorial.py

def factorial(n):
    result = 1
    counter = 1
    while counter <= n:
        result *= counter
        counter += 1
    return result

n = 5
print(f"The factorial of {n} is {factorial(n)}")
