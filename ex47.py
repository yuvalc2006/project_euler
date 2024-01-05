def count_prime_divs(x):
    div = 2
    count = 0
    while div <= x:
        if_div = False
        while x % div == 0:
            if_div = True
            x //= div
        if if_div:
            count += 1
        div += 1
    return count


n = 4
x = 8
while True:
    i = 0
    while i < n and count_prime_divs(x + i) == n:
        i += 1
    if i == n:
        print(x)
        break
    x += 1