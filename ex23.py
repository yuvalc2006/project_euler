def sum_of_divs(x):
    div = 1
    sum1 = 0
    while div <= x // 2:
        if x % div == 0:
            sum1 += div
        div += 1
    return sum1


maximum = 28_123
x = 1
abundant_numbers = []

while x <= maximum:
    if x < sum_of_divs(x):
        abundant_numbers.append(x)
    x += 1

length_abundant_numbers = len(abundant_numbers)
help_calc_sum_of_powers_sum = 0
sum_of_abundant_numbers = set()
for i in range(length_abundant_numbers):
    for j in range(i, length_abundant_numbers):
        num1 = abundant_numbers[i]
        num2 = abundant_numbers[j]
        help_calc_sum_of_powers_sum = num1 + num2
        if help_calc_sum_of_powers_sum <= maximum:
            sum_of_abundant_numbers.add(help_calc_sum_of_powers_sum)
sum_to_max = (maximum + 1) * maximum / 2
print(sum_to_max - sum(sum_of_abundant_numbers))
