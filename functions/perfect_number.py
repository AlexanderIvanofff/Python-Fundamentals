def is_perfect_number(number):
    total_number = []
    for num in range(1, number):
        if number % num == 0:
            total_number.append(num)

    if sum(total_number) == number:
        return f'We have a perfect number!'
    else:
        return f'It\'s not so perfect.'


print(is_perfect_number(int(input())))
