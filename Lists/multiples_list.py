def multiple_list(factor, count):
    multiple = []
    for num in range(1, count + 1):
        multiple.append(num * factor)

    return multiple


print(multiple_list(int(input()), int(input())))
