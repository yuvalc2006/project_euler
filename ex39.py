p = 1
max_sols = 0
p_max_sols = p
while p <= 1_000:
    a = 1
    sols = set()
    while a <= p // 4:
        b = p*(p-2*a) / (2 * (p - a))
        if b % 1 == 0:
            sols.add(a)
        a += 1
    curr_sols = len(sols)
    if curr_sols > max_sols:
        max_sols = curr_sols
        p_max_sols = p
    p += 1
print(p_max_sols)