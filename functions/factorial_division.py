def factorial_first(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def factorial_second(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def solve(first_number, second_number):
    result =  factorial_first(first_number) / factorial_second(second_number)
    return f'{result:.2f}'


print(solve(int(input()), int(input())))
