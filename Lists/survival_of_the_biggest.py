def solve(string_of_numbers, number):
    numbers = []

    for num in string_of_numbers:
        numbers.append(int(num))

    for i in range(number):
        numbers.remove(min(numbers))
    return numbers


print(solve(input().split(), int(input())))