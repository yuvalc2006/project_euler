from math import sqrt, floor


def is_square(n):
    return sqrt(n) % 1 == 0

def find_as(x):
    steps = []
    root = sqrt(x)
    a0 = floor(root)
    a = a0
    numerator = 1
    denominator = root - a0
    b = a0
    while True:
        denominator = (x - b ** 2) / numerator
        numerator = root + b
        a = floor(numerator / denominator)
        b -= denominator * a
        numerator -= denominator * a
        step = (a, b, denominator)
        if step in steps:
            return [step[0] for step in steps]
        steps.append(step)
        temp = denominator
        denominator = numerator
        numerator = temp
        b = -b

if __name__ == '__main__':
    D = 1000
    max_x = -1
    max_d = -1
    for d in range(1, D + 1):
        if is_square(d):
            continue
        a_repeat = find_as(d)
        a_repeat_len = len(a_repeat)
        N = 1
        coefs = [floor(sqrt(d))]
        while True:
            # numerator
            num = 1
            # denominator
            denom = coefs[-1]
            for i in range(N - 1):
                a = coefs[-(i + 2)]
                num += a * denom
                temp = denom
                denom = num
                num = temp
            temp = denom
            denom = num
            num = temp
            if num**2 - d * (denom ** 2) == 1:
                if num > max_x:
                    max_x = num
                    max_d = d
                break
            coefs.append(a_repeat[(N - 1) % a_repeat_len])
            N += 1
    print(max_d, max_x)
