def solve(number_str):
    for i, n in enumerate(number_str):
        if n == 0:
            number_str.remove(n)
            number_str.append(n)

    return number_str


number_as_str = list(map(int, input().split(', ')))
print(solve(number_as_str))
