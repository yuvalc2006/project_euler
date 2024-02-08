def print_reverse_digits(reverse_arr):
    for i in range(10):
        print(reverse_arr[-(i + 1)], end='')
    print()

def add_digit(last_10_digits_backwards, index, digit):
    if index >= 10:
        return
    num = last_10_digits_backwards[index] + digit
    carry = num // 10
    while carry > 0 and index < 10:
        last_10_digits_backwards[index] = num % 10
        index += 1
        if index >= 10:
            return
        num = last_10_digits_backwards[index] + carry
        carry = num // 10
    last_10_digits_backwards[index] = num % 10

def add_arrays(arr1, arr2):
    carry = 0
    for i in range(len(arr1)):
        num = arr1[i] + arr2[i] + carry
        arr1[i] = num % 10
        carry = num // 10

def add(old_last_10_digits_backwards, n):
    last_10_digits_backwards = [1,0,0,0,0,0,0,0,0,0]
    curr_run = 0
    str_n = str(n)
    while curr_run < n:
        if curr_run == 9:
            curr_run = 9
        i = 0
        new_last_10_digits_backwards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while i < len(str_n):
            j = 0
            carry = 0
            while j < 10:
                digit = last_10_digits_backwards[j] * int(str_n[-(i + 1)]) + carry
                carry = digit // 10
                add_digit(new_last_10_digits_backwards, i + j, digit % 10)
                j += 1
            i += 1
        last_10_digits_backwards = new_last_10_digits_backwards
        curr_run += 1
    add_arrays(old_last_10_digits_backwards, last_10_digits_backwards)

arr = [1,0,0,0,0,0,0,0,0,0]
for i in range(2, 1_000 + 1):
    add(arr, i)
print_reverse_digits(arr)