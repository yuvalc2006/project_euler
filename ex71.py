import math

from tqdm import tqdm


def intercepts(a, b):
    for i in a:
        if i in b:
            return True
    return False


if __name__ == '__main__':
    n = 1_000_000
    prime_factors = [set() for i in range(n + 2)]
    target = 3 / 7
    closest = 1 / 8
    closest_num = 1

    for i in tqdm(range(2, n + 1)):
        curr_primes = prime_factors[i]
        if len(curr_primes) == 0:
            curr_primes.add(i)
            num = i
            while num <= n:
                prime_factors[num].add(i)
                num += i

        if i == 3:
            continue
        num = math.ceil(i / target)
        curr_div = i / num
        while num <= n and curr_div > closest:
            if not intercepts(curr_primes, prime_factors[num]):
                if target - curr_div < 0:
                    pass
                closest_num = i
                closest = curr_div
                break
            num += 1
            curr_div = i / num

    print(closest_num, closest)
