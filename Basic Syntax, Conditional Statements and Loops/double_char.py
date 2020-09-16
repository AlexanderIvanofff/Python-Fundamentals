def solve(string):
    result = [x * 2 for x in string]
    return ''.join(result)


print(solve(input()))