# exercise_7_compound_interest.py

def compound_interest(P, r, n, t):
    A = P * (1 + r / n) ** (n * t)
    return A

P = 1000  # principal
r = 0.05  # interest rate (5%)
n = 4     # times compounded per year
t = 5     # time in years

print(f"The compound interest after {t} years is: {compound_interest(P, r, n, t):.2f}")
