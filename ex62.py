if __name__ == '__main__':
    num_perms = 5
    permutations_cubes = {}
    n = 1
    while True:
        cube = n ** 3
        cube_copy = cube
        digits_appearances = [0] * 10
        while cube > 0:
            curr_digit = cube % 10
            digits_appearances[curr_digit] += 1
            cube = cube // 10
        digits_appearances_str = str(digits_appearances)
        if digits_appearances_str in permutations_cubes:
            permutations_cubes[digits_appearances_str].append(cube_copy)
            if len(permutations_cubes[digits_appearances_str]) == num_perms:
                print(min(permutations_cubes[digits_appearances_str]))
                break
        else:
            permutations_cubes[digits_appearances_str] = [cube_copy]
        n += 1
