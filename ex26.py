#this algorithm is based on fraction long division
x = 2
max_num = 1_000
max_repeat_length = 0
max_repeat_length_num = 0
arr = []
help_calc_sum_of_powers_number = 10
repeat_length = 0
d = 0
m = 0
s = 0
while x < max_num:
    if x % 2 != 0 and x % 5 != 0:
        help_calc_sum_of_powers_number = 10
        arr = []
        repeat_length = 0
        while True:
            # d stands for divide
            d = help_calc_sum_of_powers_number // x
            # m stands for multiply
            m = d * x
            # s stand for subtract
            s = help_calc_sum_of_powers_number - m
            # help_calc_sum_of_powers_number is bringing down the next digit but because it is always 0 we just multiply 10 to add a zero
            help_calc_sum_of_powers_number = s * 10
            # if help_calc_sum_of_powers_number is already in the array we've entered a loop which means we've found the repeating part
            if help_calc_sum_of_powers_number in arr:
                repeat_length = len(arr)
                if repeat_length > max_repeat_length:
                    max_repeat_length = repeat_length
                    max_repeat_length_num = x
                break
            arr.append(help_calc_sum_of_powers_number)
    x += 1
print(max_repeat_length_num)