from math import sqrt

def is_triangle_num(x):
    if ((-1 + sqrt(1 + 8 * x)) / 2) % 1 == 0:
        return True
    return False

with open('C:\\Users\\yuval\\PycharmProjects\\project_euler\\ex42_names.txt', 'r') as file:
    line = file.read()
    line = line.strip('"')
    words = line.split('","')

    count = 0
    for word in words:
        i = 0
        sum_letter_values = 0
        while i < len(word):
            sum_letter_values += ord(word[i]) - ord('A') + 1
            i += 1
        if is_triangle_num(sum_letter_values):
            count += 1
print(count)