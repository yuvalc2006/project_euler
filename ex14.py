def collatz(x):
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1


x = 2
help_calc_sum_of_powers_x = 2
steps_to_one = [1]
max_steps = 0
num_max_steps = 0
while x < 1_000_000:
    steps = 0
    help_calc_sum_of_powers_x = x
    while not help_calc_sum_of_powers_x < x:
        steps += 1
        help_calc_sum_of_powers_x = collatz(help_calc_sum_of_powers_x)
    steps += steps_to_one[help_calc_sum_of_powers_x - 1]
    if steps > max_steps:
        num_max_steps = x
        max_steps = steps
    steps_to_one.append(steps)
    x += 1
print(num_max_steps)
