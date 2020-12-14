cards = input().split(', ')
n = int(input())

for index in range(n):
    tokens = input().split(', ')

    instruction = tokens[0]
    if instruction == 'Add':
        card_name = tokens[1]
        if card_name in cards:
            print(f'Card is already bought')
        else:
            print(f'Card successfully bought')
            cards.append(card_name)

    elif instruction == 'Remove':
        card = tokens[1]
        if card in cards:
            print(f'Card successfully sold')
            cards.remove(card)
        else:
            print(f'Card not found')

    elif instruction == 'Remove At':
        index = int(tokens[1])
        if index not in range(len(cards)):
            print(f'Index out of range')
        else:
            cards.pop(index)
            print(f'Card successfully sold')

    elif instruction == 'Insert':
        first_index = int(tokens[1])
        cards_name = tokens[2]

        if first_index not in range(len(cards)):
            print(f'Index out of range')
            continue
        elif cards_name not in cards:
            cards.insert(first_index, cards_name)
            print(f'Card successfully bought')
        else:
            print(f'Card is already bought')

print(', '.join(cards))