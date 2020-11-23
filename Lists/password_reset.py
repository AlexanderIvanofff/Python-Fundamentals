password = input()

command = input()

while not command == 'Done':
    tokens = command.split()

    instruction = tokens[0]
    current_string = ''
    if instruction == 'TakeOdd':
        for index in range(len(password)):
            if index % 2 != 0:
                current_string += password[index]
        password = current_string
        print(password)

    elif instruction == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])

        fist_str = password[:index]
        second_str = password[index + length:]
        password = fist_str + second_str
        print(password)

    elif instruction == 'Substitute':
        substring = tokens[1]
        substitute = tokens[2]

        if substring not in password:
            print(f'Nothing to replace!')
        else:
            password = password.replace(substring, substitute)
            print(password)

    command = input()

print(f'Your password is: {password}')