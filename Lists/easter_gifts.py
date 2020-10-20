gifts = input().split()


def get_out_of_stock(items):
    gift = tokens[1]

    for index in range(len(items)):
        if gift in items[index]:
            items.pop(index)
            items.insert(index, str(None))


def get_requaried(items):
    gift = tokens[1]
    index = int(tokens[2])

    if index in range(len(items)):
        items.pop(index)
        items.insert(index, str(gift))


def get_just_in_case(items):
    gift = tokens[1]
    for index in range(len(items)):
        items.pop(-1)
        items.append(gift)


while True:
    command = input()
    if command == 'No Money':
        break

    tokens = command.split()
    instructions = tokens[0]

    if instructions == 'OutOfStock':
        get_out_of_stock(gifts)

    elif instructions == 'Required':
        get_requaried(gifts)

    elif instructions == 'JustInCase':
        get_just_in_case(gifts)


final = [x for x in gifts if x != 'None']

print(f'{" ".join(final)}')