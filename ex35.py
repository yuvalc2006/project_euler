def generate_primes(limit_primes):
    sieve = [True] * (limit_primes + 1)
    sieve[0] = sieve[1] = False
    for y in range(2, limit_primes // + 1):
        curr = 2 * y
        while curr <= limit_primes:
            sieve[curr] = False
            curr += y
    return sieve


def are_rotations_prime(x, rotations_made):
    if rotations_made > len(x):
        return True
    if not primes[int(x)]:
        return False
    new_x = x[1:] + x[0]
    return are_rotations_prime(new_x, rotations_made + 1)


limit = 1_000_000
primes = generate_primes(limit)
x = 2
count = 0
while x < limit:
    if primes[x] and are_rotations_prime(str(x), 0):
        count += 1
    x += 1
print(count)

# the code I made initially because I didn't understand the question and solved a harder problem
"""
def generate_primes(limit_primes):
    sieve = [True] * (limit_primes + 1)
    sieve[0] = sieve[1] = False
    for y in range(2, limit_primes // + 1):
        curr = 2 * y
        while curr <= limit_primes:
            sieve[curr] = False
            curr += y
    return sieve


def change_char_at_index(input_string, index, new_char):
    if 0 <= index < len(input_string):
        # Create a new string with the modified character at the specified index
        result_string = input_string[:index] + new_char + input_string[index + 1:]
        return result_string
    else:
        print("Index out of range.")
        return input_string


def are_all_combs_prime(digits, current, index):
    if len(current) == len(digits):
        return primes[int(current)]
    if index >= len(digits):
        return True
    i = 0
    while i < len(digits):
        digit = digits[i]
        if digit != '!':
            digits = change_char_at_index(digits, i, '!')
            if not are_all_combs_prime(digits, current + digit, index + 1):
                return False
            digits = change_char_at_index(digits, i, digit)
        i += 1
    return True


limit = 1000000
primes = generate_primes(limit)
x = 2
count = 0
while x < limit:
    if x == 197:
    if primes[x] and are_all_combs_prime(str(x), "", 0):
        count += 1
    x += 1
print(count)
"""
