# just a slightly edited ex71

import math

from tqdm import tqdm


def intercepts(a, b):
    for i in a:
        if i in b:
            return True
    return False


if __name__ == '__main__':
    n = 12_000
    prime_factors = [set() for i in range(n + 2)]
    upper = 1/2
    lower = 1/3
    count = 0

    for i in tqdm(range(2, n + 1)):
        curr_primes = prime_factors[i]
        if len(curr_primes) == 0:
            curr_primes.add(i)
            num = i
            while num <= n:
                prime_factors[num].add(i)
                num += i

        num = math.ceil(i / upper)
        curr_div = i / num
        while num <= n and curr_div > lower:
            if not intercepts(curr_primes, prime_factors[num]):
                count += 1
            num += 1
            curr_div = i / num

    print(count)
