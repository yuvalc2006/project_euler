def prime_product(x):
    div = 2
    while div <= x:
        while x % div == 0:
            if div in primes:
                primes[div] += 1
            else:
                primes[div] = 1
            x //= div
        div += 1


min_divisors = 5
index = 1
primes = {}
num_of_divs = 1
num = 0
while True:
    primes = {}
    if index % 2 == 0:
        num = (index // 2) * (index + 1)
        prime_product(index // 2)
        prime_product(index + 1)
    else:
        num = index * (index + 1) / 2
        prime_product(index)
        prime_product((index + 1) / 2)
    num_of_divs = 1
    for key in primes:
        num_of_divs *= (primes[key] + 1)
    if num_of_divs > 500:
        print(num)
        break
    index += 1