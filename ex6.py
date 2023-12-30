sum_of_squares = 0
sum = 0
square_of_sum = 0
upper_bound = 100
for i in range(1, upper_bound + 1):
    sum += i
    sum_of_squares += i**2
square_of_sum = sum**2
print(square_of_sum - sum_of_squares)