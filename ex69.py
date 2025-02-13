# my original solution was not optimal, made this with a bit of outside help.

from tqdm import tqdm

if __name__ == '__main__':
    n = 1_000_000
    phi = [1] * (n + 1)
    phi[1] = 1
    prime = [True] * (n + 1)

    for i in tqdm(range(2, n + 1)):
        if not prime[i]:
            continue

        num = i

        while num <= n:
            prime[num] = False
            phi[num] /= (1 - 1/i)
            num += i
    max_div = max(phi)
    print(phi.index(max_div), max_div)
