from math import sqrt


def is_prime(x):
    div = 2
    if x < 2:
        return False
    while div < int(sqrt(x)) + 1:
        if div * div > x:
            return True
        if x % div == 0:
            return False
        div += 1
    return True


def gen_primes_until(help_calc_sum_of_powers_a, help_calc_sum_of_powers_b):
    n = 0
    while True:
        if not is_prime(n ** 2 + help_calc_sum_of_powers_a * n + help_calc_sum_of_powers_b):
            return n - 1
        n += 1


max_primes_gen = 0
help_calc_sum_of_powers_primes_gen = 0
a_max = 0
b_max = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        help_calc_sum_of_powers_primes_gen = gen_primes_until(a, b)
        if help_calc_sum_of_powers_primes_gen > max_primes_gen:
            max_primes_gen = help_calc_sum_of_powers_primes_gen
            a_max = a
            b_max = b
print(a_max * b_max)
