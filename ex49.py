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


def change_char_at_index(input_string, index, new_char):
    if 0 <= index < len(input_string):
        # Create a new string with the modified character at the specified index
        result_string = input_string[:index] + new_char + input_string[index + 1:]
        return result_string
    else:
        print("Index out of range.")
        return input_string


def find_prime_combs(digits, current, index):
    if len(current) == len(digits):
        if is_prime[int(current)]:
            permutations.add(int(current))
    if index >= len(digits):
        return
    i = 0
    while i < len(digits):
        digit = digits[i]
        if digit != '!':
            digits = change_char_at_index(digits, i, '!')
            find_prime_combs(digits, current + digit, index + 1)
            digits = change_char_at_index(digits, i, digit)
        i += 1


def check_permutations(digits):
    return find_prime_combs(digits, "", 0)

# this is a solution for the general question where "const" is unknown, it's based on my first solution to ex35
limit = 10_000
is_prime = generate_primes(limit)
permutations = set()
x = 2
const = 0
primes = [num for num in range(2, limit) if is_prime[num]]
final = []

for x in primes:
    permutations = set()
    check_permutations(str(x))
    for prime1 in permutations:
        const = prime1 - x
        if const > 0:
            prime2 = x + 2 * const
            if prime2 in permutations:
                final.append(int(str(x) + str(prime1) + str(prime2)))
print(final)