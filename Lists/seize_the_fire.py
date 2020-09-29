level_of_fire = input().split('#')
count_of_water = int(input())

effort = 0
total_fire = 0
print(f'Cells:')
for fire in level_of_fire:
    type_of_data = fire.split(' = ')

    type_of_fire = type_of_data[0]
    fire_range = int(type_of_data[1])

    if count_of_water < fire_range:
        continue

    if type_of_fire == 'High':
        if 81 <= fire_range <= 125:
            print(f' - {fire_range}')
            effort += fire_range * 0.25
            total_fire += fire_range
            count_of_water -= fire_range

    elif type_of_fire == 'Medium':
        if 51 <= fire_range <= 80:
            print(f' - {fire_range}')
            effort += fire_range * 0.25
            total_fire += fire_range
            count_of_water -= fire_range

    elif type_of_fire == 'Low':
        if 1 <= fire_range <= 50:
            print(f' - {fire_range}')
            effort += fire_range * 0.25
            total_fire += fire_range
            count_of_water -= fire_range
    else:
        continue


print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')