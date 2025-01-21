def get_len(x):
    length = 0
    while x > 0:
        length += 1
        x //= 10
    return length


if __name__ == '__main__':
    limit = 1000
    count = 0
    power = 1
    while power < limit:
        # 10 to the power of "power" is 1 with "power" 0s, which is too long so that's our upper limit
        num = 9
        num_powered = num ** power
        while get_len(num_powered) == power:
            count += 1
            num -= 1
            num_powered = num ** power
        power += 1
    print(count)
