import math


def find_period(x):
    steps = set()
    root = math.sqrt(x)
    a0 = math.floor(root)
    a = a0
    numerator = 1
    denominator = root - a0
    b = a0
    for i in range(limit):
        denominator = (x - b ** 2) / numerator
        numerator = root + b
        a = math.floor(numerator / denominator)
        b -= denominator * a
        numerator -= denominator * a
        step = (a, b, denominator)
        if step in steps:
            return i
        steps.add(step)
        temp = denominator
        denominator = numerator
        numerator = temp
        b = -b


def is_perfect_square(x):
    return math.sqrt(x) % 1 == 0


if __name__ == '__main__':
    limit = 10000
    N = 10000
    count = 0
    for n in range(2, N + 1):
        if is_perfect_square(n):
            continue
        if find_period(n) % 2 == 1:
            count += 1
    print(count)
