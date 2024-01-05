#sol1
start_num = 1
start = 1
digits = 1
end = 10
end_num = 10
places_in_product = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
final_mult = 1
while start <= 1_000_000:
    while len(places_in_product) > 0 and start <= places_in_product[0] < end:
        num = start_num + (places_in_product[0] - start) // digits
        index_in_num = (num - start) % digits
        final_mult *= int(str(num)[index_in_num])
        places_in_product.pop(0)
    digits += 1
    start = end
    start_num = end_num
    end += 9 * (10 ** (digits - 1)) * digits
    end_num = 10**digits
print(final_mult)

#sol2
x = 1
digit = 0
mult = 1
while digit <= 1_000_000:
    str_x = str(x)
    i = 0
    while i < len(str_x):
        digit += 1
        curr_digit = int(str_x[i])
        if digit in [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]:
            mult *= curr_digit
        i += 1
    x += 1
print(mult)