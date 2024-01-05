from math import sqrt


def is_triangular(x):
    if ((-1 + sqrt(1 + 8 * x)) / 2) % 1 == 0:
        return True
    return False


def is_pentagonal(x):
    if ((1 + sqrt(1 + 24 * x)) / 6) % 1 == 0:
        return True
    return False


def is_hexagonal(x):
    if ((1 + sqrt(1 + 8 * x)) / 4) % 1 == 0:
        return True
    return False


index = (1 + sqrt(1 + 8 * 40_755)) // 4 + 1
while True:
    x = index * (2 * index - 1)
    if is_triangular(x) and is_pentagonal(x) and is_hexagonal(x):
        print(x)
        break
    index += 1
