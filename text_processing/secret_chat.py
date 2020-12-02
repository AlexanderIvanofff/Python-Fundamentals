message = input()

command = input()
while not command == 'Reveal':
    tokens = command.split(':|:')
    instructions = tokens[0]

    if instructions == 'InsertSpace':
        index = int(tokens[1])
        message = message[:index] + ' ' + message[index:]
        print(message)

    elif instructions == 'Reverse':
        substring = tokens[1]

        if substring in message:
            message = message.replace(substring, '', 1)
            message += substring[::-1]
            print(message)
        else:
            print('error')

    elif instructions == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]

        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f'You have a new text message: {message}')