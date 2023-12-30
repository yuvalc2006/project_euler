dictionary = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7,
              16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7}
x = 1
length_of_number_name = 0
sum_of_lengths = 0
first_two_digits = 0
hundreds = 0
while x < 1_000:
    length_of_number_name = 0
    first_two_digits = x % 100
    if first_two_digits in dictionary:
        length_of_number_name += dictionary[first_two_digits]
    else:
        length_of_number_name += dictionary[first_two_digits % 10]
        length_of_number_name += dictionary[first_two_digits - (first_two_digits % 10)]
    hundreds = x // 100
    if hundreds != 0:
        if first_two_digits != 0:
            length_of_number_name += 3  # adding 'and'
        length_of_number_name += dictionary[hundreds]
        length_of_number_name += 7  # adding 'hundred'
    print(f"the number is {x} and it's length is {length_of_number_name}")
    sum_of_lengths += length_of_number_name
    x += 1
print(sum_of_lengths + 11)
