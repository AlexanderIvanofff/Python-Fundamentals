quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_light = 15

day = 1
budget = 0
christmas_spirit = 0

while day <= days:
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        budget += ornament_set * quantity
        christmas_spirit += 5

    if day % 3 == 0:
        budget += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13

    if day % 5 == 0:
        budget += tree_light * quantity
        christmas_spirit += 17

    if day % 15 == 0:
        christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_garlands + tree_light

    day += 1

if days % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')