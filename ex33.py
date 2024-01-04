mult = 1
for den in range(10, 100):
    digits = [den // 10, den % 10]
    if den == 24:
        x = 1
    if digits[1] != 0:
        for curr in range(1, digits[1]):
            if curr / digits[1] >= 1:
                break
            if curr / digits[1] == (digits[0] * 10 + curr) / den:
                print("a ", digits[0] * 10 + curr, den)
                mult *= curr / digits[1]
        for curr in range(1, digits[0]):
            if curr / digits[0] >= 1:
                break
            if curr / digits[1] == (curr * 10 + digits[0]) / den:
                print("b ", curr * 10 + digits[0], den)
                mult *= curr / digits[1]
        for curr in range(1, digits[0]):
            if curr / digits[0] >= 1:
                break
            if curr / digits[0] == (curr * 10 + digits[1]) / den:
                print("c ", curr * 10 + digits[1], den)
                mult *= curr / digits[0]
        for curr in range(1, 10):
            if curr / digits[0] >= 1:
                break
            if curr / digits[0] == (digits[1] * 10 + curr) / den:
                print("d ", curr * 10 + digits[1], den)
                mult *= curr / digits[0]
# mult is 0.01 so the denominator is 100
print(mult)