max_spiral_size = 1_001


def sum_diagonal(n, sum_of_diag, max_prev):
    spiral_size = 2 * n - 1
    if spiral_size > max_spiral_size:
        return sum_of_diag
    steps_to_next = spiral_size - 1
    first_num_in_spiral = max_prev + 1
    sum_of_diag += first_num_in_spiral + steps_to_next - 1
    sum_of_diag += first_num_in_spiral + 2 * steps_to_next - 1
    sum_of_diag += first_num_in_spiral + 3 * steps_to_next - 1
    sum_of_diag += first_num_in_spiral + 4 * steps_to_next - 1
    return sum_diagonal(n + 1, sum_of_diag, first_num_in_spiral + 4 * steps_to_next - 1)


print(sum_diagonal(2, 1, 1))
