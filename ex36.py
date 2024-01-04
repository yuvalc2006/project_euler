def is_binary_palindrom(x):
    bin_digits_backwards = []
    while x > 0:
        if x % 2 == 0:
            bin_digits_backwards.append(0)
        else:
            bin_digits_backwards.append(1)
        x //= 2
    i = 0
    while i < len(bin_digits_backwards) // 2:
        if bin_digits_backwards[i] != bin_digits_backwards[-(i + 1)]:
            return False
        i += 1
    return True

def is_palindrome(str_x):
    i = 0
    while i < len(str_x) // 2:
        if str_x[i] != str_x[-(i + 1)]:
            return False
        i += 1
    return True
x = 1
sum_of_double_palindromes = 0
while x <= 1_000_000:
    if is_binary_palindrom(x) and is_palindrome(str(x)):
        sum_of_double_palindromes += x
    x += 1
print(sum_of_double_palindromes)