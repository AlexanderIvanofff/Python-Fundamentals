number = list(map(int, input().split()))

while True:
    command = input()
    if command == 'END':
        break

    tokens = command.split()
    instructions = tokens[0]

    if instructions == 'Change':
        painting_number = int(tokens[1])
        changed_number = int(tokens[2])

        if painting_number in number:
            index = number.index(painting_number)
            number.pop(index)
            number.insert(index, changed_number)

    elif instructions == 'Hide':
        painting_numbers = int(tokens[1])
        if painting_numbers in number:
            number.remove(painting_numbers)

    elif instructions == 'Switch':
        first_number = int(tokens[1])
        second_number = int(tokens[2])

        if first_number in number and second_number in number:
            first_index = number.index(first_number)
            second_index = number.index(second_number)
            number[first_index], number[second_index] = number[second_index], number[first_index]

    elif instructions == 'Insert':
        place = int(tokens[1])
        num = int(tokens[2])

        if place in range(len(number)):
            number.insert(place + 1, num)

    elif instructions == 'Reverse':
        number = number[::-1]


print(*number)
