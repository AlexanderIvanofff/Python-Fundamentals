email = input()

command = input()
while not command == 'Complete':
    tokens = command.split()
    instructions = tokens[0]

    if command == 'Make Upper':
        email = email.upper()
        print(email)
    elif command == 'Make Lower':
        email = email.lower()
        print(email)

    elif instructions == 'GetDomain':
        count = int(tokens[1])
        domain = email[-count:]
        print(domain)

    elif instructions == 'GetUsername':
        if '@' not in email:
            print(f'The email {email} does\'t contain the @ symbol.')
        else:
            token = email.split('@')
            print(token[0])

    elif instructions == 'Replace':
        char = tokens[1]
        email = email.replace(char, "-")
        print(email)

    elif instructions == 'Encrypt':
        for char in email:
            print(ord(char), end=' ')
    command = input()
