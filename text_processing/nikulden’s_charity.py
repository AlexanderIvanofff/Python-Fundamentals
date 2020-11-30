text = input()

command = input()
while not command == 'Finish':
    tokens = command.split()
    instructions = tokens[0]

    if instructions == 'Replace':
        current_char = tokens[1]
        new_char = tokens[2]
        text = text.replace(current_char, new_char)
        print(text)

    elif instructions == 'Cut':
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if start_index not in range(len(text)) or end_index not in range(len(text)):
            print(f'Invalid indexes!')
        else:
            text = list(text)
            del text[start_index:end_index+1]
            text = "".join(text)
            print(text)

    elif instructions == 'Make':
        type_str = tokens[1]
        if type_str == 'Upper':
            text = text.upper()
            print(text)

        elif type_str == 'Lower':
            text = text.lower()
            print(text)

    elif instructions == 'Check':
        string = tokens[1]
        if string in text:
            print(f'Message contains {string}')
        else:
            print(f'Message doesn\'t contain {string}')

    elif instructions == 'Sum':
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if start_index not in range(len(text)) or end_index not in range(len(text)):
            print(f'Invalid indexes!')
        else:
            total = 0
            total_text = text[start_index:end_index + 1]
            for char in total_text:
                total += ord(char)
            print(total)

    command = input()