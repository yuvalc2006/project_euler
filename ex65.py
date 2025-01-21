def sum_of_digits(x):
    dig_sum = 0
    while x > 0:
        dig_sum += x % 10
        x //= 10
    return dig_sum


def generate_coefficient_list(n):
    coef_list = [2]  # The sequence starts with 2
    for i in range(1, n):
        if i % 3 == 2:  # Every third position (2, 5, 8, ...)
            coef_list.append(2 * (i // 3 + 1))  # Append 2k
        else:
            coef_list.append(1)  # Append 1 for other positions
    return coef_list


if __name__ == '__main__':
    N = 100  # Number of terms to generate
    coefs = generate_coefficient_list(N)
    n = 1
    d = coefs[-1]
    for i in range(N - 1):
        a = coefs[-(i + 2)]
        n += a * d
        temp = d
        d = n
        n = temp
    temp = d
    d = n
    n = temp
    print(sum_of_digits(n))
