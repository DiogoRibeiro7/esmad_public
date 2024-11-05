# exercise_2_series_sum.py

def series_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    return result

n = 10
print(f"The sum of the series up to {n} terms is {series_sum(n)}")
