from tqdm import tqdm


def get_digit_count(x):
    digs = {}
    while x > 0:
        dig = x % 10
        if dig in digs:
            digs[dig] += 1
        else:
            digs[dig] = 1
        x //= 10
    return digs


def is_perm(x, y):
    return get_digit_count(x) == get_digit_count(y)


def update_min(curr_min_div, i, phi_i, curr_min_div_n):
    if i == 87109:
        pass
    if not is_perm(i, phi_i):
        return curr_min_div_n, curr_min_div
    curr_div = i / phi_i
    if curr_min_div > curr_div:
        return i, i / phi_i
    return curr_min_div_n, curr_min_div


if __name__ == '__main__':
    n = 10 ** 7
    phi = [i for i in range(n + 2)]
    prime = [True] * (n + 1)
    min_div = float('inf')
    min_div_n = -1

    for i in tqdm(range(2, n + 1)):
        if not prime[i]:
            min_div_n, min_div = update_min(min_div, i, phi[i], min_div_n)
            continue

        num = i

        while num <= n:
            prime[num] = False
            phi[num] *= (1 - 1 / i)
            num += i
        min_div_n, min_div = update_min(min_div, i, phi[i], min_div_n)
    print(min_div_n, min_div)
