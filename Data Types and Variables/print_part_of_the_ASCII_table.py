def solve(start_number, end_number):
    for char in range(start_number, end_number + 1):
        print(chr(char), end=' ')


solve(int(input()), int(input()))