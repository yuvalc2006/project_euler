from math import sqrt

def is_pentagonal(x):
    if ((1 + sqrt(1 + 24 * x)) / 6) % 1 == 0:
        return True
    return False

def generate_pentagonals(limit):
    count = 0
    arr = []
    x = 1
    while count < limit:
        if is_pentagonal(x):
            count += 1
            arr.append(x)
        x += 1
    return arr

def special_min(a, b):
    if a == -1:
        return b
    if b == -1:
        return a
    return min(a, b)

lim = 3_000
pentagonals = generate_pentagonals(lim)
D = -1
for index1 in range(lim):
    for index2 in range(index1 + 1, lim):
        if is_pentagonal(pentagonals[index2] - pentagonals[index1]) and is_pentagonal(pentagonals[index1] + pentagonals[index2]):
            D = special_min(D, abs(pentagonals[index1] - pentagonals[index2]))
print(D)
