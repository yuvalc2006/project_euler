from math import sqrt
import sys


def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_array[mid] == target:
            return True  # Target found, return the index
        elif sorted_array[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return False  # Target not found


def special_min(a, b):
    if a == -1:
        return b
    if b == -1:
        return a
    return min(a, b)


def regurlar_is_prime(x, arr):
    for div in arr:
        if div * div > x:
            return True
        if x % div == 0:
            return False
    return True


primes = []
for i in range(2, 10_000):
    if regurlar_is_prime(i, primes):
        primes.append(i)

possible_primes = []
for i in range(2, 100_000_000):
    if regurlar_is_prime(i, possible_primes):
        possible_primes.append(i)
len_primes = len(primes)
arr_size = 5


def is_prime(x):
    return binary_search(possible_primes, x)


def find_lowest_sum(index, old_curr_primes, made_a_change):
    curr_primes = old_curr_primes[:]
    index_last_curr_prime = len(curr_primes) - 1
    if made_a_change:
        for i in range(0, index_last_curr_prime):
            if not is_prime(int(str(curr_primes[i]) + str(curr_primes[index_last_curr_prime]))) or not is_prime(
                    int(str(curr_primes[index_last_curr_prime]) + str(curr_primes[i]))):
                return -1
    if index_last_curr_prime == arr_size - 1:
        return sum(curr_primes)
    if index >= len_primes:
        return -1
    no_change = find_lowest_sum(index + 1, curr_primes, made_a_change=False)
    curr_primes.append(primes[index])
    yes_change = find_lowest_sum(index + 1, curr_primes, made_a_change=True)
    return special_min(yes_change, no_change)


sys.setrecursionlimit(3000)
print(find_lowest_sum(0, [], False))
