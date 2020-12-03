n = int(input())
heroes = {}


def cast_spell(hero_dict, hero_names, mp_needed, spell_names):
    if heroes[hero_names][1] >= mp_needed:
        heroes[hero_names][1] -= mp_needed
        print(f'{hero_names} has successfully cast {spell_names} and now has {heroes[hero_names][1]} MP!')
    else:
        print(f'{hero_names} does not have enough MP to cast {spell_names}!')
    return hero_dict


def take_damage(hero_dict, hero_names, current_damage, current_attacker):
    hero_dict[hero_names][0] -= current_damage
    if hero_dict[hero_names][0] > 0:
        print(f'{hero_names} was hit for {current_damage} HP by {current_attacker} and now has {hero_dict[hero_names][0]} HP left!')
    else:
        del hero_dict[hero_names]
        print(f'{hero_names} has been killed by {current_attacker}!')
    return hero_dict


def recharge(hero_dict, hero_names, current_amount):
    if hero_dict[hero_names][1] + current_amount <= 200:
        hero_dict[hero_names][1] += current_amount
        print(f'{hero_names} recharged for {current_amount} MP!')
    else:
        total = abs(hero_dict[hero_names][1] - 200)
        hero_dict[hero_names][1] += total
        print(f'{hero_names} recharged for {total} MP!')
    return hero_dict


def heal(hero_dict, hero_names, current_amount):
    if hero_dict[hero_names][0] + current_amount <= 100:
        hero_dict[hero_names][0] += current_amount
        print(f'{hero_names} healed for {current_amount} HP!')
    else:
        total = abs(100 - hero_dict[hero_names][0])
        hero_dict[hero_names][0] += total
        print(f'{hero_names} healed for {total} HP!')
    return hero_dict


for _ in range(n):
    hero_name, health, mana = input().split()
    health = int(health)
    mana = int(mana)

    heroes[hero_name] = [health, mana]

command = input()


while not command == 'End':
    tokens = command.split(' - ')
    instructions = tokens[0]
    name = tokens[1]

    if instructions == 'CastSpell':
        MP_needed = int(tokens[2])
        spell_name = tokens[3]
        heroes = cast_spell(heroes, name, MP_needed, spell_name)

    elif instructions == 'TakeDamage':
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes = take_damage(heroes, name, damage, attacker)

    elif instructions == 'Recharge':
        amount = int(tokens[2])
        heroes = recharge(heroes, name, amount)

    elif instructions == 'Heal':
        amount = int(tokens[2])
        heroes = heal(heroes, name, amount)

    command = input()

for kay, value in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{kay}\n  HP: {value[0]}\n  MP: {value[1]}')