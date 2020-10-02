def solve(first_chr, second_chr):
    total_char = []
    for char in range(ord(first_chr) + 1, ord(second_chr)):
        total_char.append(chr(char))

    return ' '.join(total_char)


print(solve(input(), input()))

