x = 6
index = 3
while index <= 10:
    if index % 2 == 0:
        x *= 3 + (index // 2 - 1) / (index // 2)
    else:
        x *= 3 + (index - 2) / index
    index += 1
print(x)
"""
THIS IS THE CODE I WANTED BUT IT'S NOT FAST ENOUGH, THE ACTUAL CODE IS JUST AN OBSERVATION I MADE ABOUT SMALLER VALUES OF n

def out_of_bounds(row, col):
    if row < 0 or not row < n + 1 or col < 0 or not col < n + 1:
        return True
    return False


def find_num_of_paths(row, col):
    if out_of_bounds(row, col):
        return 0
    if row == n and col == n:
        return 1
    return find_num_of_paths(row + 1, col) + find_num_of_paths(row, col + 1)


prev = 6
now = 6
for i in range(3, 13):
    n = i
    prev = now
    now = find_num_of_paths(0, 0)
    print (now / prev)
"""