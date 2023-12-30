class Binary_tree:
    value = None
    sum_max_path = None
    right_son = None
    left_son = None

    def __init__(self, value, left_son, right_son):
        self.value = value
        self.right_son = right_son
        self.left_son = left_son
        if left_son is None and left_son is None:
            self.sum_max_path = int(value)
        else:
            self.sum_max_path = int(value) + max(right_son.sum_max_path, left_son.sum_max_path)


# this is the same code as ex67 on a different file
with open('ex18_pyramid.txt', 'r') as file:
    lines = file.readlines()
    line = []
    next_line = []
    lines_in_file = len(lines)
    line_num = lines_in_file - 1
    index = 0
    numbers_in_line = 0
    nodes_next_line = []
    nodes_this_line = []

    while line_num > -1:
        next_line = line
        line = lines[line_num].split()
        nodes_next_line = nodes_this_line
        nodes_this_line = []

        if not line:
            break

        index = 0
        numbers_in_line = len(line)
        while index < numbers_in_line:
            if not next_line:
                nodes_this_line.append(Binary_tree(line[index], None, None))
            else:
                nodes_this_line.append(Binary_tree(line[index], nodes_next_line[index], nodes_next_line[index + 1]))
            index += 1
        line_num -= 1
    print(nodes_this_line[0].sum_max_path)
