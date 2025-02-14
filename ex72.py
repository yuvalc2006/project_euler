from tqdm import tqdm
import itertools


if __name__ == '__main__':
    n = 1_000_000
    prime_factors = [set() for i in range(n + 2)]
    # to include everything with nominator of 1
    size = n - 1

    for i in tqdm(range(2, n + 1)):
        curr_primes = prime_factors[i]
        if len(curr_primes) == 0:
            curr_primes.add(i)
            num = i
            while num <= n:
                prime_factors[num].add(i)
                num += i

        curr_size = n - i

        power_set = []
        for r in range(1, len(curr_primes) + 1):
            for subset in itertools.combinations(curr_primes, r):
                mul = 1
                for p in subset:
                    mul *= p
                amount = (n - i) // mul
                if r % 2 == 0:
                    curr_size += amount
                else:
                    curr_size -= amount
        size += curr_size

    print(size)
