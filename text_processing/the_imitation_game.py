message = input()

command = input()
while not command == 'Decode':
    tokens = command.split('|')
    instructions = tokens[0]

    if instructions == 'Move':
        count = int(tokens[1])
        message = message[count:]+message[:count]

    elif instructions == 'Insert':
        index = int(tokens[1])
        value = tokens[2]

        message = list(message)
        message.insert(index, value)
        message = "".join(message)

    elif instructions == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        message = message.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {message}')