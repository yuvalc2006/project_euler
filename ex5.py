x = 2
arr = []
upper_bound = 20
while x <= upper_bound:
    help_calc_sum_of_powers = x
    for index in arr:
        if help_calc_sum_of_powers % index == 0:
            help_calc_sum_of_powers /= index
    if help_calc_sum_of_powers != 1:
        arr.append(help_calc_sum_of_powers)
    x += 1
l = 1
for i in arr:
    l *= i
print(l)