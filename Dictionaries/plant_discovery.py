def rate(plant_dict, current_name, current_rating):
    if current_name in plant_dict:
        plant_dict[current_name]["Rating"].append(current_rating)
    else:
        print('error')
    return plant_dict


def update(plant_dict, current_name, n_rarity):
    if current_name in plant_dict:
        plant_dict[current_name]["Rarity"] = n_rarity
    else:
        print('error')
    return plant_dict


def reset(plant_dict, current_name):
    if current_name in plant_dict:
        plant_dict[current_name]["Rating"].clear()
    else:
        print('error')
    return plant_dict


n = int(input())
plant_discovery = {}

for _ in range(n):
    data = input().split('<->')

    name = data[0]
    current_rarity = int(data[1])

    plant_discovery[name] = {'Rarity': current_rarity, 'Rating': []}

command = input()

while not command == 'Exhibition':
    data = command.split(': ')

    instructions = data[0]
    tokens = data[1].split(' - ')

    if instructions == 'Rate':
        plant_name = tokens[0]
        rating = int(tokens[1])
        plant_discovery = rate(plant_discovery, plant_name, rating)

    elif instructions == 'Update':
        plant_name = tokens[0]
        new_rarity = int(tokens[1])
        plant_discovery = update(plant_discovery, plant_name, new_rarity)

    elif instructions == 'Reset':
        plant_name = tokens[0]
        plant_discovery = reset(plant_discovery, plant_name)

    command = input()


for kay, value in plant_discovery.items():
    if not len(value["Rating"]) == 0:
        plant_discovery[kay]["Rating"] = sum(plant_discovery[kay]['Rating']) / len(plant_discovery[kay]["Rating"])
    else:
        plant_discovery[kay]["Rating"] = 0

print("Plants for the exhibition:")
for kay, value in sorted(plant_discovery.items(), key=lambda x: (-x[1]['Rarity'], -x[1]["Rating"])):
    print(f"- {kay}; Rarity: {value['Rarity']}; Rating: {value['Rating']:.2f}")