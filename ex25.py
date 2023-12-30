digits_backwards1 = [1]
digits_backwards2 = [1]
new_number_backwards = [2]
carry = 0
digit_index = 0
num_of_digits = 0
help_calc_sum_of_powers = 0
index = 3
while True:
    carry = 0
    help_calc_sum_of_powers = 0
    digit_index = 0
    num_of_digits = len(digits_backwards1)
    new_number_backwards = []
    while digit_index < num_of_digits:
        if digit_index < len(digits_backwards2):
            help_calc_sum_of_powers = digits_backwards1[digit_index] + digits_backwards2[digit_index] + carry
        else:
            help_calc_sum_of_powers = digits_backwards1[digit_index] + carry
        new_number_backwards.append(help_calc_sum_of_powers % 10)
        carry = help_calc_sum_of_powers // 10
        digit_index += 1
    while carry != 0:
        new_number_backwards.append(carry % 10)
        carry //= 10
    digits_backwards2 = digits_backwards1
    digits_backwards1 = new_number_backwards
    if len(digits_backwards1) >= 1_000:
        break
    index += 1
print(index)