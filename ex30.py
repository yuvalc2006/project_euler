power = 5

upper_bound = 1_000_000
x = 2
help_calc_sum_of_powers = 0
sum_power_of_digits = 0
final_sum = 0
while x < upper_bound:
    help_calc_sum_of_powers = x
    sum_power_of_digits = 0
    while help_calc_sum_of_powers > 0:
        sum_power_of_digits += (help_calc_sum_of_powers % 10) ** power
        help_calc_sum_of_powers //= 10
    if sum_power_of_digits == x:
        final_sum += x
    x += 1
print(final_sum)