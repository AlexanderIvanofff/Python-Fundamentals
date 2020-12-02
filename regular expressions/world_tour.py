string = input()

command = input()
while not command == 'Travel':
    tokens = command.split(':')
    instructions = tokens[0]

    if instructions == 'Add Stop':
        index = int(tokens[1])
        current_string = tokens[2]

        if index in range(len(string)):
            string = string[:index] + current_string + string[index:]
            print(string)
        else:
            print(string)

    elif instructions == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if start_index in range(len(string)) and end_index in range(len(string)):
            string = string[:start_index] + string[end_index+1:]
            print(string)
        else:
            print(string)

    elif instructions == 'Switch':
        old_string = tokens[1]
        new_string = tokens[2]

        if old_string in string:
            string = string.replace(old_string, new_string)
            print(string)
        else:
            print(string)
    command = input()

print(f'Ready for world tour! Planned stops: {string}')