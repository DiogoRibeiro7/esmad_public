# exercise_3_prime_check.py

def is_prime(n):
    """Check if a number is prime."""#+
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 7
print(f"{n} is {'a prime number' if is_prime(n) else 'not a prime number'}")
