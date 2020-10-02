def solve(number):
    number = str(number)
    odd_number = []
    even_number = []
    for num in number:
        if int(num) % 2 == 0:
            even_number.append(int(num))
        else:
            odd_number.append(int(num))

    return ''.join(f'Odd sum = {sum(odd_number)}, Even sum = {sum(even_number)}')


print(solve(int(input())))