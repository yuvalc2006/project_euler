import math

from tqdm import tqdm


def update_dict(dict, l, tuple):
    if l not in dict:
        return
    if len(dict[l]) == 0:
        dict[l].extend(tuple)
        return
    rec_a = tuple[0]
    rec_b = tuple[1]
    curr_a = dict[l][0]
    curr_b = dict[l][1]
    if (rec_a == curr_a and rec_b == curr_b) or (rec_a == curr_b and rec_b == curr_a):
        return
    del dict[l]


def intercepts(a, b):
    for i in a:
        if i in b:
            return True
    return False


if __name__ == '__main__':
    n = 1_500_000
    lim = math.floor(math.sqrt(n / 2))
    prime_factors = [set() for i in range(n + 2)]
    count = 0
    lengths_count = {i: [] for i in range(n + 1)}

    for i in tqdm(range(1, n + 1)):
        curr_primes = prime_factors[i]
        if i != 1 and len(curr_primes) == 0:
            curr_primes.add(i)
            num = i
            while num <= n:
                prime_factors[num].add(i)
                num += i
        if i == 1:
            pass
        num = i + 1
        while num <= lim:
            if not intercepts(curr_primes, prime_factors[num]) and not (i % 2 == 1 and num % 2 == 1):
                a0 = num ** 2 - i ** 2
                b0 = 2 * i * num
                c0 = i ** 2 + num ** 2

                a = a0
                b = b0
                c = c0

                curr_len0 = a + b + c
                curr_len = curr_len0
                while curr_len <= n:
                    update_dict(lengths_count, curr_len, [a, b, c])
                    a += a0
                    b += b0
                    c += c0
                    curr_len += curr_len0
            num += 1
    for key, value in lengths_count.items():
        if len(value) == 3:
            count += 1
    print(count)
