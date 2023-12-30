lower_bound = 2
upper_bound = 100
combs = set()

for a in range(lower_bound, upper_bound + 1):
    for b in range(lower_bound, upper_bound + 1):
        combs.add(a**b)
print(len(combs))