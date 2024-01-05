from math import log10


def num_length(x):
    return int(log10(x)) + 1


def binary_search_first_occurrence(multi):
    low, high = 1, 987654321
    target_length = 9 - num_length(multi)
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        curr_length = num_length(mid) + num_length(multi * mid)

        if curr_length == target_length:
            result = mid
            high = mid - 1  # Look for the first occurrence in the left half
        elif curr_length < target_length:
            low = mid + 1
        else:
            high = mid - 1

    return result


def is_pan(x):
    digits = [x for x in range(1, 10)]
    while x > 0:
        digit = x % 10
        if digit not in digits:
            return False
        digits.remove(digit)
        x //= 10
    if not digits:
        return True
    return False


results = set()
multiplicand = 1
while True:
    multiplier = binary_search_first_occurrence(multiplicand)
    if multiplier == -1:
        break
    while num_length(multiplicand) + num_length(multiplier) + num_length(multiplier * multiplicand) == 9:
        if is_pan(int(f"{multiplicand}{multiplier}{multiplier * multiplicand}")):
            results.add(multiplier * multiplicand)
        multiplier += 1
    multiplicand += 1
print(sum(results))
