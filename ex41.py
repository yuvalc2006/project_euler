def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check for divisibility from 3 to the square root of the number
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


def max_prime_pan(digits, current):
    if len(current) == len(digits):
        if is_prime(int(current)):
            return int(current)
        else:
            return -1
    i = 0
    results = []
    while i < len(digits):
        digit = digits[i]
        if digit != '!':
            digits[i] = '!'
            results.append(max_prime_pan(digits, current + str(digit)))
            digits[i] = digit
        i += 1
    return max(results)


result = -1
n = 10
while result == -1:
    n -= 1
    result = max_prime_pan([i for i in range(1, n + 1)], "")
print(n, result)
