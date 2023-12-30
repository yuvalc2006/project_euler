from math import factorial as fact


def find_combination(digits, combination_number, combination):
    if not digits:
        return True
    digit_index = combination_number // fact(len(digits) - 1)
    combination_number = combination_number % fact(len(digits) - 1)
    combination.append(digits[digit_index])
    digits.pop(digit_index)
    find_combination(digits, combination_number, combination)


max_digit = 9
comb_n = 1_000_000
c = []
d = [i for i in range(max_digit + 1)]
find_combination(d, comb_n - 1, c)
print(c)
