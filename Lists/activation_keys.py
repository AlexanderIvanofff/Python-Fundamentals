letters_and_numbers = input()

command = input()
while not command == 'Generate':
    tokens = command.split('>>>')
    instructions = tokens[0]

    if instructions == 'Contains':
        string = tokens[1]
        if string in letters_and_numbers:
            print(f'{letters_and_numbers} contains {string}')
        else:
            print(f'Substring not found!')

    elif instructions == 'Flip':
        type_string = tokens[1]
        first_index = int(tokens[2])
        count_index = int(tokens[3])

        if type_string == 'Upper':
            first = letters_and_numbers[:first_index]
            second_part = letters_and_numbers[first_index:count_index].upper()
            final = letters_and_numbers[count_index:]
            letters_and_numbers = first + second_part + final
            print(letters_and_numbers)

        elif type_string == 'Lower':
            first = letters_and_numbers[:first_index]
            second_part = letters_and_numbers[first_index:count_index].lower()
            final = letters_and_numbers[count_index:]
            letters_and_numbers = first + second_part + final
            print(letters_and_numbers)

    elif instructions == 'Slice':
        index = int(tokens[1])
        count = int(tokens[2])

        first_part = letters_and_numbers[:index]
        second_part = letters_and_numbers[count:]
        letters_and_numbers = first_part + second_part
        print(letters_and_numbers)

    command = input()

print(f'Your activation key is: {letters_and_numbers}')
