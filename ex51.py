def generate_primes(limit_primes):
    sieve = [True] * (limit_primes + 1)
    sieve[0] = sieve[1] = False
    for y in range(2, limit_primes // 2 + 1):
        if sieve[y]:
            curr = 2 * y
            while curr <= limit_primes:
                sieve[curr] = False
                curr += y
    return sieve


# def func(length, )

max_num = 0
max_num_vars = 0


def check_gen_nums(x, indexes, index):
    global max_num_vars
    global max_num
    if index >= len(x):
        if index in indexes:
            indexes.remove(index)
        if not indexes:
            return
        variations_that_are_prime = 0
        len_x = len(x)
        for digit in range(0, 10):
            i = len_x - 1
            curr = 0
            while i > -1:
                if i in indexes:
                    curr += digit * 10 ** (len_x - i - 1)
                else:
                    curr += int(x[i]) * 10 ** (len_x - i - 1)
                i -= 1
            if not (0 in indexes and digit == 0) and is_prime[curr]:
                variations_that_are_prime += 1
        if variations_that_are_prime > max_num_vars:
            print(variations_that_are_prime, x, indexes)
            max_num_vars = variations_that_are_prime
            max_num = int(x)
        return
    check_gen_nums(x, indexes + [index + 1], index + 1)
    check_gen_nums(x, indexes, index + 1)


def check_gen_nums_help(x):
    check_gen_nums(x, [], 0)
    check_gen_nums(x, [0], 0)


limit = 1_000_000
is_prime = generate_primes(limit)
x = 1
wanted_vars = 8
while True:
    if is_prime[x]:
        check_gen_nums_help(str(x))
        if max_num_vars == wanted_vars:
            print(max_num)
            break
    x += 1
# the answer is 120383 where I switch digits 1, 3 and 5, so the smallest prime in that family is 121313

"""
this is the code I used to check and go over my answer:

from ex51 import generate_primes

limit = 1_000_000
is_prime = generate_primes(limit)

x = "120383"
indexes = [0, 2, 4]
len_x = len(x)
variations_that_are_prime = 0
for digit in range(0, 10):
    i = len_x - 1
    curr = 0
    while i > -1:
        if i in indexes:
            curr += digit * 10 ** (len_x - i - 1)
        else:
            curr += int(x[i]) * 10 ** (len_x - i - 1)
        i -= 1
    print(curr, is_prime[curr])