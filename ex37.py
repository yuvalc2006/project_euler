def generate_primes(limit_primes):
    sieve = [True] * (limit_primes + 1)
    sieve[0] = sieve[1] = False
    for y in range(2, limit_primes // + 1):
        curr = 2 * y
        while curr <= limit_primes:
            sieve[curr] = False
            curr += y
    return sieve


def is_truncatable_left(x):
    starting_index = 0
    while starting_index < len(x):
        if not primes[int(x[starting_index:])]:
            return False
        starting_index += 1
    return True


def is_truncatable_right(x):
    ending_index = 0
    while ending_index < len(x):
        if not primes[int(x[:len(x) - ending_index])]:
            return False
        ending_index += 1
    return True


prime_digits = ['2', '3', '5', '7']
limit = 1_000_000
primes = generate_primes(limit)
x = 11
sum_truncatable_primes = 0
while x <= limit:
    str_x = str(x)
    if is_truncatable_left(str_x) and is_truncatable_right(str_x):
        sum_truncatable_primes += x
    x += 1
print(sum_truncatable_primes)
