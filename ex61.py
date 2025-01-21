import math


def get_triangle(n):
    return n * (n + 1) / 2


def get_square(n):
    return n * n


def get_penta(n):
    return n * (3 * n - 1) / 2


def get_hexa(n):
    return n * (2 * n - 1)


def get_hepta(n):
    return n * (5 * n - 3) / 2


def get_octa(n):
    return n * (3 * n - 2)


def get_n_from_triangle(T):
    return (-1 + math.sqrt(1 + 8 * T)) / 2


def get_n_from_square(S):
    return math.sqrt(S)


def get_n_from_penta(P):
    return (1 + math.sqrt(1 + 24 * P)) / 6


def get_n_from_hexa(H):
    return (1 + math.sqrt(1 + 8 * H)) / 4


def get_n_from_hepta(He):
    return (3 + math.sqrt(9 + 40 * He)) / 10


def get_n_from_octa(O):
    return (2 + math.sqrt(4 + 12 * O)) / 6


get_num_from_n = {
    1: get_triangle,
    2: get_square,
    3: get_penta,
    4: get_hexa,
    5: get_hepta,
    6: get_octa
}

get_n = {
    1: get_n_from_triangle,
    2: get_n_from_square,
    3: get_n_from_penta,
    4: get_n_from_hexa,
    5: get_n_from_hepta,
    6: get_n_from_octa
}


def find_set(num, stages_left):
    if num < 1000 or num >= 10000:
        return -1
    if stages_left == []:
        if num % 100 == triangle_num // 100:
            return 0
        return -1
    for stage in stages_left:
        new_num_floor = (num % 100) * 100
        new_num_ceil = new_num_floor + 100
        this_n = math.ceil(get_n[stage](new_num_floor))
        new_num = get_num_from_n[stage](this_n)
        while new_num < new_num_ceil:
            sum_of_nums = find_set(new_num, [s for s in stages_left if s != stage])
            if sum_of_nums != -1:
                print(f"{stage}: {new_num}")
                return sum_of_nums + new_num
            this_n += 1
            new_num = get_num_from_n[stage](this_n)
    return -1


if __name__ == '__main__':
    max_n = 6
    curr_n = math.ceil(get_n_from_triangle(1000))
    triangle_num = get_triangle(curr_n)
    while triangle_num < 10000:
        if triangle_num == 8128:
            pass
        curr_sum = find_set(triangle_num, [i for i in range(2, max_n + 1)])
        if curr_sum != -1:
            print(f"1: {triangle_num}")
            print(f"sum: {curr_sum + triangle_num}")
            break
        curr_n += 1
        triangle_num = get_triangle(curr_n)
