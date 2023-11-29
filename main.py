def eratosthenes(n):
    numbers = list(range(2, n + 1))
    primes = []

    while numbers:
        current_prime = numbers[0]
        primes.append(current_prime)
        numbers = [num for num in numbers if num % current_prime != 0]

    return primes

limit = 30
result = eratosthenes(limit)
print(f"Простые числа до {limit}: {result}")
