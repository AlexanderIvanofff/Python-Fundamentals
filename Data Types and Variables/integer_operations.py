def solve(first_number, second_number, third_number, four_number):
    add = first_number + second_number
    divide = add // third_number
    multiply = divide * four_number
    return multiply


print(solve(int(input()), int(input()), int(input()), int(input())))

