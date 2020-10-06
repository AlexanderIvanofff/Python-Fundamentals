def solve(numbers):
    num = list(map(lambda x: int(x), numbers.split(', ')))

    even_num = []
    for index in range(len(num)):
        if num[index] % 2 == 0:
            even_num.append(index)

    return even_num


print(solve(input()))