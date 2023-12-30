def is_same_number_scrambled(digits1, digits2):
    if len(digits1) != len(digits2):
        return False

    count_dict = {}

    for digit in digits1:
        count_dict[digit] = count_dict.get(digit, 0) + 1

    for digit in digits2:
        if digit not in count_dict or count_dict[digit] == 0:
            return False
        count_dict[digit] -= 1

    return True


digits_x = ""
digits_new = ""
x = 1
upper_bound = 6
end = False
while True:
    digits_new = ""
    digits_x = ""
    digits_x = str(x)
    end = True
    for i in range(2, upper_bound + 1):
        digits_new = str(i*x)
        if not is_same_number_scrambled(digits_x, digits_new):
            end = False
            break
    if end:
        print(x)
        break
    x += 1
