from math import sqrt


def is_prime(x):
    for div in range(2, int(sqrt(x)) + 1):
        if x % div == 0:
            return False
    return True


count = 0
max_count = 10_001
x = 2

while count < max_count:
    if is_prime(x):
        count += 1
    x += 1
print(x - 1)
