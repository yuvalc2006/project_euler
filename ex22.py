with open('C:\\Users\\tomer\\projects\\ex22_names.txt', 'r') as file:
    line = file.read()
    line = line.strip('"')
    names = line.split('","')
    names.sort()

    sum_of_scores = 0
    sum_ab_value = 0

    name_index = 0
    name_length = 0
    char_index = 0
    num_of_names = len(names)
    while name_index < num_of_names:
        char_index = 0
        name_length = len(names[name_index])
        sum_ab_value = 0
        while char_index < name_length:
            sum_ab_value += (ord(names[name_index][char_index]) - ord('A') + 1)
            char_index += 1
        sum_of_scores += sum_ab_value * (name_index + 1)
        name_index += 1
    print(sum_of_scores)