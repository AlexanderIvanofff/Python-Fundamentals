houses = list(map(int, input().split('@')))

last_position = 0
while True:
    command = input()
    if command == 'Love!':
        break
    tokens = command.split()

    instructions = tokens[0]
    index = int(tokens[1])

    current_position = last_position + index

    if current_position >= len(houses):
        current_position = 0

    if houses[current_position] > 0:
        houses[current_position] -= 2

        if houses[current_position] == 0:
            print(f'Place {current_position} has Valentine\'s day.')
    else:
        print(f'Place {current_position} already had Valentine\'s day.')

    last_position = current_position

print(f'Cupid\'s last position was {last_position}.')
if sum(houses) == 0:
    print(f'Mission was successful.')

else:
    total_count = []
    for index, items in enumerate(houses):
        if items > 0:
            total_count.append(index)

    print(f'Cupid has failed {len(total_count)} places.')
