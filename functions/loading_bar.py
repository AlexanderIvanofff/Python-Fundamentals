def loading_bar(input_number):
    bar = ['.'] * 10
    current_number = input_number // 10

    for i in range(current_number):
        bar[i] = '%'

    return bar


def solve(number):
    if number < 100:
        return f'{number}% [{"".join(loading_bar(number))}] \nStill loading... '
    else:
        return f'{number}% Complete!\n[{"".join(loading_bar(number))}]'


numbers = int(input())
print(solve(numbers))
