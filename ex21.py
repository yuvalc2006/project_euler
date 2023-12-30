def sum_of_divs(x):
    div = 1
    sum1 = 0
    while div <= x // 2:
        if x % div == 0:
            sum1 += div
        div += 1
    return sum1


x = 1
dictionary = {}
sum_of_amicable = 0
while x < 10_000:
    sum_of_divisors = sum_of_divs(x)
    if x in dictionary and sum_of_divisors in dictionary[x]:
        sum_of_amicable += x
        sum_of_amicable += sum_of_divisors
        dictionary[x].remove(sum_of_divisors)
    if sum_of_divisors in dictionary:
        dictionary[sum_of_divisors].append(x)
    else:
        dictionary[sum_of_divisors] = [x]


    x += 1
print(sum_of_amicable)