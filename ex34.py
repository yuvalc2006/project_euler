x = 3
curr = 0
x_digits_fact = 0
digit_fact = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5_040, 8: 40_320, 9: 362_880}
limit = 100_000
overall_sum = 0

while x < limit:
    curr = x
    x_digits_fact = 0
    while curr != 0:
        x_digits_fact += digit_fact[curr % 10]
        curr //= 10
    if x_digits_fact == x:
        overall_sum += x
    x += 1
print(overall_sum)