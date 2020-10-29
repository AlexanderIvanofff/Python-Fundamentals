painting_number = list(map(int, input().split()))

while True:
    command = input()
    if command == 'END':
        break

    tokens = command.split()

    instructions = tokens[0]

    if instructions == 'Change':
        painting_numbers = int(tokens[1])
        changedNumber = int(tokens[2])

        for index in range(len(painting_number)):
            if painting_numbers == painting_number[index]:
                painting_number.pop(index)
                painting_number.insert(index, changedNumber)

    elif instructions == 'Hide':
        painting_numbers = int(tokens[1])
        if painting_numbers in painting_number:
            painting_number.remove(painting_numbers)

    elif instructions == 'Switch':
        painting_numbers = int(tokens[1])
        paintingNumber2 = int(tokens[2])
        if painting_numbers in painting_number and paintingNumber2 in painting_number:
            first_index = painting_number.index(painting_numbers)
            second_index = painting_number.index(paintingNumber2)
            painting_number[first_index], painting_number[second_index] = \
                painting_number[second_index], painting_number[first_index]

    elif instructions == 'Insert':
        index = int(tokens[1])
        painting_numbers = int(tokens[2])

        if index in range(len(painting_number)):
            painting_number.insert(index + 1, painting_numbers)

    elif instructions == 'Reverse':
        painting_number = list(filter(lambda x: x, reversed(painting_number)))


print(*painting_number)