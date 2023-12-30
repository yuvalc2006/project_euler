count = 0
n = 1
while n <= 100:
    help_calc_sum_of_powers = 1
    for r in range(1, n + 1):
        #nCr = nC(r-1) * ((n-r+1) / r)
        help_calc_sum_of_powers *= (n - r + 1) / r
        if help_calc_sum_of_powers > 1_000_000:
            count += 1
    n += 1
print(count)