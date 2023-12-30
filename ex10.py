def is_prime(x):
    for div in arr:
        if div * div > x:
            return True
        if x % div == 0:
            return False
    return True


upper_bound = 2_000_000
x = 2
sum_of_primes = 0
arr = []
while x <= upper_bound:
    print(x)
    if is_prime(x):
        arr.append(x)
    x += 1
for item in arr:
    sum_of_primes += item
print(sum_of_primes)
