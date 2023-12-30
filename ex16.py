x = 2**1_000
sum_of_digits = 0
while x > 0:
    sum_of_digits += x % 10
    x //= 10
print(sum_of_digits)