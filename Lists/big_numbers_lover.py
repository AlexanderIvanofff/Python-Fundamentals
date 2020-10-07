def solve(number_str):
    number_str.sort(reverse=True)
    return ''.join(number_str)


str = input().split()
print(solve(str))