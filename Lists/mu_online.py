dungeons_rooms = input().split('|')

bitcoins = 0
health = 100
current_index = 0
dungeons_len = len(dungeons_rooms)


while health > 0:
    for index in dungeons_rooms:
        tokens = index.split()

        type_meet = tokens[0]
        count = int(tokens[1])

        if type_meet == 'potion':
            if health + count >= 100:
                current_health = abs(health - 100)
                health += current_health
                print(f'You healed for {current_health} hp.')
                print(f'Current health: {health} hp.')
            else:
                health += count
                print(f'You healed for {count} hp.')
                print(f'Current health: {health} hp.')

        elif type_meet == 'chest':
            bitcoins += count
            print(f'You found {count} bitcoins.')

        else:
            health -= count

            if health > 0:
                print(f'You slayed {type_meet}.')
            else:
                print(f'You died! Killed by {type_meet}.')
                current_index = dungeons_rooms.index(index)
                print(f'Best room: {current_index + 1}')
                break
        current_index += 1

        if dungeons_len == current_index:
            print(f'You\'ve made it!')
            print(f'Bitcoins: {bitcoins}')
            print(f'Health: {health}')
            exit()