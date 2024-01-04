def is_pandigital(str_x):
    digits = "123456789"
    index = 0
    while index < 9:
        if digits[index] not in str_x:
            return False
        index += 1
    return True


n = 2
max_pan = 0
while n < 10:
    x = 1
    while True:
        str_pan = ""
        for i in range(1, n + 1):
            str_pan = str_pan + str(x * i)
        len_str_pan = len(str_pan)
        if len_str_pan > 9:
            break
        if len_str_pan == 9 and is_pandigital(str_pan) and int(str_pan) > max_pan:
            max_pan = int(str_pan)
        x += 1
    n += 1
print(max_pan)