def invert_values(strings):
    reverse_str = []
    for num_str in strings:
        number = -int(num_str)
        reverse_str.append(number)

    return reverse_str


print(invert_values(input().split(' ')))
