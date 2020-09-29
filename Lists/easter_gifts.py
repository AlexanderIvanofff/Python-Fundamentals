gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    tokens = command.split()

    type_of_command = tokens[0]
    gift = tokens[1]

    if type_of_command == 'OutOfStock':
        for index, current_gift in enumerate(gifts):
            if current_gift == gift:
                gifts[index] = 'None'

    elif type_of_command == 'Required':
        index = int(tokens[2])
        if 0 <= index <= len(gifts):
            gifts[index] = gift

    elif type_of_command == 'JustInCase':
        gifts[-1] = gift

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))