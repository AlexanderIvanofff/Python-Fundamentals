number = int(input())

for digit in range(1, number + 1):
    sum_of_digit = 0

    for c in str(digit):
        sum_of_digit += int(c)

    is_special = sum_of_digit in (5, 7, 11)
    print(f'{digit} -> {is_special}')