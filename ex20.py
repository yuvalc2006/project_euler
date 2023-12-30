digits_backwards = [1]
n = 100
x = 2
carry = 0
digit_index = 0
num_of_digits = 0
help_calc_sum_of_powers = 0
while x <= n:
    carry = 0
    digit_index = 0
    help_calc_sum_of_powers = 0
    num_of_digits = len(digits_backwards)
    while digit_index < num_of_digits:
        help_calc_sum_of_powers = digits_backwards[digit_index] * x + carry
        digits_backwards[digit_index] = help_calc_sum_of_powers % 10
        carry = help_calc_sum_of_powers // 10
        digit_index += 1
    while carry != 0:
        digits_backwards.append(carry % 10)
        carry //= 10
    x += 1
sum_of_digits = sum(digits_backwards)
print(digits_backwards)