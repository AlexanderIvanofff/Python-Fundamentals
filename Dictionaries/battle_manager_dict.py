def add(manager_dict, current_person_name, current_health, current_energy):
    if current_person_name not in manager_dict:
        manager_dict[current_person_name] = {"health": current_health, "energy": current_energy}
    else:
        manager_dict[current_person_name] += {"health": current_health}
    return manager_dict


def attack(manager_dict, current_attacker_name, current_defender_name, current_damage):
    if current_attacker_name in manager_dict and current_defender_name in manager_dict:
        manager_dict[current_defender_name]["health"] -= current_damage
        manager_dict[current_attacker_name]["energy"] -= 1
        if manager_dict[current_defender_name]["health"] <= 0:
            del manager_dict[current_defender_name]
            print(f'{current_defender_name} was disqualified!')
        if manager_dict[current_attacker_name]["energy"] <= 0:
            del manager_dict[current_attacker_name]
            print(f'{current_attacker_name} was disqualified!')
    return manager_dict


def delete(manager_dict, current_username):
    if current_username == 'All':
        manager_dict.clear()
    else:
        del manager_dict[current_username]
    return manager_dict


manager_info = {}

command = input()

while not command == 'Results':
    tokens = command.split(':')
    instructions = tokens[0]

    if instructions == 'Add':
        person_name = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])
        manager_info = add(manager_info, person_name, health, energy)

    elif instructions == 'Attack':
        attacker_name = tokens[1]
        defender_name = tokens[2]
        damage = int(tokens[3])

        manager_info = attack(manager_info, attacker_name, defender_name, damage)

    elif instructions == 'Delete':
        username = tokens[1]
        manager_info = delete(manager_info, username)

    command = input()

print(f'People count: {len(manager_info)}')

for kay, value in sorted(manager_info.items(), key=lambda x: (-x[1]["health"], x[0])):
    print(f'{kay} - {value["health"]} - {value["energy"]}')