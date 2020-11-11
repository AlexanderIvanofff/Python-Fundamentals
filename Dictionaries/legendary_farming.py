from collections import defaultdict


def print_dict(dictionary, template):
    for kay, value in dictionary.items():
        print(template.format(kay, value))


kay_materials = {
    'fragments': 0,
    'shards': 0,
    'motes': 0,
}

legendary_items = {
    'fragments': 'Valanyr',
    'shards': 'Shadowmourne',
    'motes': 'Dragonwrath',
}

junks = defaultdict(int)
winner = ''

while winner == '':
    tokens = input().lower().split()

    for index in range(0, len(tokens), 2):
        quantity = int(tokens[index])
        material = tokens[index + 1]

        if material in kay_materials:
            kay_materials[material] += quantity
            if kay_materials[material] >= 250:
                winner = material
                break
        else:
            junks[material] += quantity


kay_materials[winner] -= 250
winner_item = legendary_items[winner]

print(f'{winner_item} obtained!')

kay_materials = dict(sorted(kay_materials.items(), key=lambda x: (-x[1], x[0])))
junks = dict(sorted(junks.items()))

print_dict(kay_materials, "{}: {}")
print_dict(junks, "{}: {}")