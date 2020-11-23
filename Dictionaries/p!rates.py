from collections import defaultdict

command = input()
cities = defaultdict(list)

while not command == 'Sail':
    tokens = command.split('||')
    town = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])

    if town not in cities.keys():
        cities[town] = [population, gold]
    else:
        cities[town][0] += population
        cities[town][1] += gold

    command = input()

command = input()

while not command == 'End':
    tokens = command.split('=>')
    instruction = tokens[0]

    if instruction == 'Plunder':
        town = tokens[1]
        population = int(tokens[2])
        gold = int(tokens[3])

        cities[town][0] -= population
        cities[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {population} citizens killed.')

        if cities[town][0] <= 0 or cities[town][1] <= 0:
            cities.pop(town)
            print(f'{town} has been wiped off the map!')

    elif instruction == 'Prosper':
        town = tokens[1]
        gold = int(tokens[2])

        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')

    command = input()
if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')

    for key, value in sorted(cities.items(), key=lambda x: (-x[1][1], x[0])):
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')

else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')