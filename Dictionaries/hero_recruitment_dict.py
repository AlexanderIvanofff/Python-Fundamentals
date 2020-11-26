command = input()

heroes = {}
while not command == 'End':
    tokens = command.split()
    instruction = tokens[0]
    hero_name = tokens[1]

    if instruction == 'Enroll':
        if hero_name in heroes.keys():
            print(f'{hero_name} is already exist.')
        heroes[hero_name] = []

    elif instruction == 'Learn':
        spell_name = tokens[2]

        if hero_name not in heroes.keys():
            print(f"{hero_name} does't exist.")

        elif spell_name in heroes[hero_name]:
            print(f'{hero_name} has already learn.')
        else:
            heroes[hero_name].append(spell_name)

    elif instruction == 'Unlearn':
        spell_name = tokens[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} does't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} does't know {spell_name}")
        else:
            heroes[hero_name].remove(spell_name)

    command = input()
print(f"Heroes:")
for hero, spells in sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f'== {hero}:', end=' ')
    print(', '.join(spells))
