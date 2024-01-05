from math import sqrt


def generate_primes(limit_primes):
    sieve = [True] * (limit_primes + 1)
    sieve[0] = sieve[1] = False
    for y in range(2, limit_primes // + 1):
        curr = 2 * y
        while curr <= limit_primes:
            sieve[curr] = False
            curr += y
    return sieve


limit = 10_000
primes = generate_primes(limit)
x = 3
while True:
    p = x
    while p >= 2:
        if primes[p] and sqrt((x - p) / 2) % 1 == 0:
            break
        p -= 1
    if p < 2:
        print(x)
        break
    x += 2
