def generate_primes(limit_primes):
    sieve = [True] * (limit_primes + 1)
    sieve[0] = sieve[1] = False
    curr_primes = []
    for y in range(2, limit_primes // 2 + 1):
        if sieve[y]:
            curr_primes.append(y)
            curr = 2 * y
            while curr <= limit_primes:
                sieve[curr] = False
                curr += y
    return curr_primes

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return True  # Target found
        elif mid_value < target:
            low = mid + 1  # Adjust the search range to the right half
        else:
            high = mid - 1  # Adjust the search range to the left half

    return False  # Target not found

limit = 1_000_000
primes = generate_primes(limit)
max_len = 0
max_sum = 0
sum_all = sum(primes)
sum_all_index = len(primes) - 1
while sum_all > 0:
    curr_sum = sum_all
    for i in range(0, sum_all_index):
        if curr_sum <= limit:
            curr_len = sum_all_index - i + 1
            if curr_len < max_len:
                break
            if binary_search(primes, curr_sum):
                max_len = curr_len
                max_sum = curr_sum
                break
            curr_sum -= primes[i]
    sum_all -= primes[sum_all_index]
    sum_all_index -= 1
print(max_sum)