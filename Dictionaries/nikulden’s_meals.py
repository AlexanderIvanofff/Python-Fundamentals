command = input()

guest_list = {}
unlike_meal = 0
while not command == 'Stop':
    tokens = command.split('-')
    type_taste = tokens[0]

    guest = tokens[1]
    meal = tokens[2]

    if type_taste == 'Like':
        if guest not in guest_list:
            guest_list[guest] = []

        if meal in guest_list[guest]:
            continue
        else:
            guest_list[guest].append(meal)

    elif type_taste == 'Unlike':
        if guest not in guest_list:
            print(f'{guest} is not at the party.')
            command = input()
            continue

        if meal not in guest_list[guest]:
            print(f'{guest} doesn\'t have the {meal} in his/her collection.')
            command = input()
            continue

        guest_list[guest].remove(meal)
        unlike_meal += 1
        print(f'{guest} doesn\'t like the {meal}.')

    command = input()

for name, meal in sorted(guest_list.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f'{name}: {", ".join(meal)}')

print(f'Unliked meals: {unlike_meal}')