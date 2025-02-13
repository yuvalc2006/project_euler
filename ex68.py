def str_cus(x):
    if x == 10:
        return 'X'
    return str(x)

def int_cus(x):
    if x == 'X':
        return 10
    return int(x)

def long_int(x):
    num = 0
    for d in x:
        if d == 'X':
            num *= 100
            num += 10
        else:
            num *= 10
            num += int(d)
    return num

def int_len(x):
    l = 0
    while x > 0:
        l += 1
        x //= 10
    return l

def find_max_gon(curr_str, n):
    num_of_nodes_with_reps = 3 * n
    num_of_nodes_no_reps = 2 * n
    curr_len = len(curr_str)
    if curr_len == num_of_nodes_with_reps:
        min_ext = min([int_cus(curr_str[3 * i]) for i in range(n)])
        start = curr_str.index(str_cus(min_ext))
        num = long_int(curr_str[start:] + curr_str[:start])
        if int_len(num) == 16:
            return num
        return -1
    line_num = curr_len // 3
    index_in_line = curr_len % 3
    if curr_len == num_of_nodes_with_reps - 1:
        if int_cus(curr_str[0]) + int_cus(curr_str[1]) + int_cus(curr_str[2]) != int_cus(curr_str[-1]) + int_cus(curr_str[-2]) + int_cus(curr_str[1]):
            return -1
        return find_max_gon(curr_str + curr_str[1], n)
    if index_in_line == 1 and line_num != 0:
        return find_max_gon(curr_str + str_cus(curr_str[curr_len - 2]), n)
    max_opt = -1
    if line_num > 0:
        line_sum = int_cus(curr_str[0]) + int_cus(curr_str[1]) + int_cus(curr_str[2])
        if index_in_line == 2:
            curr_i = line_sum - int_cus(curr_str[-1]) - int_cus(curr_str[-2])
            if 0 < curr_i <= num_of_nodes_no_reps and str_cus(curr_i) not in curr_str:
                return find_max_gon(curr_str + str_cus(curr_i), n)
            else:
                return -1
    for i in range(1, num_of_nodes_no_reps + 1):
        str_i = str_cus(i)
        if str_i not in curr_str:
            curr_opt = find_max_gon(curr_str + str_i, n)
            if curr_opt > max_opt:
                max_opt = curr_opt
    return max_opt


def main():
    print(find_max_gon("", 5))


if __name__ == '__main__':
    main()