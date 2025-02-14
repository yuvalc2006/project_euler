from tqdm import tqdm


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    lim = 1_000_000
    wanted_len = 60
    count = 0
    for n in tqdm(range(lim + 1)):
        history = set()
        while True:
            if n in history:
                break
            history.add(n)
            new_n = 0
            while n > 0:
                new_n += factorial(n % 10)
                n = n // 10
            n = new_n
        if len(history) == wanted_len:
            count += 1
    print(count)
