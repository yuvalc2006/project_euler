def conditions(x):
    i = 1
    primes = [2, 3, 5, 7, 11, 13, 17]
    while i <= 7:
        if int(x[i] + x[i + 1] + x[i + 2]) % primes[i - 1] != 0:
            return False
        i += 1
    return True


def sum_pan_with_conditions(digits, current):
    if len(current) == len(digits):
        if conditions(current):
            return int(current)
        else:
            return 0
    i = 0
    sum_pan = 0
    while i < len(digits):
        digit = digits[i]
        if digit != '!':
            digits[i] = '!'
            sum_pan += sum_pan_with_conditions(digits, current + str(digit))
            digits[i] = digit
        i += 1
    return sum_pan


print(sum_pan_with_conditions([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ""))
