from collections import defaultdict

sides = defaultdict(list)

commands = input()

while not commands == 'Lumpawaroo':
    if ' | ' in commands:
        tokens = commands.split(' | ')
        side = tokens[0]
        users = tokens[1]

        all_values = []

        for current_list in sides.values():
            all_values += current_list

        if users not in all_values:
            sides[side].append(users)

    else:
        tokens = commands.split(' -> ')
        users = tokens[0]
        side = tokens[1]

        old_side = ''
        for kay, value in sides.items():
            if users in value:
                old_side = kay
                break

        if old_side != '':
            sides[old_side].remove(users)
            sides[side].append(users)
        else:
            if users not in sides:
                sides[side].append(users)
        print(f'{users} joins the {side} side!')

    commands = input()

sorted_sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for kay, value in sorted_sides.items():
    if len(value) == 0:
        continue
    print(f'Side: {kay}, Members: {len(value)}')

    for user in sorted(value):
        print(f'! {user}')