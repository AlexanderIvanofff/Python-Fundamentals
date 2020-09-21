party_size = int(input())
days = int(input())

coins = 0
for day in range(1, days + 1):

    if day % 10 == 0:
        party_size -= 2

    if day % 15 == 0:
        party_size += 5
        coins -= 2 * party_size

    coins += 50 - (2 * party_size)

    if day % 3 == 0:
        coins -= 3 * party_size

    if day % 5 == 0:
        coins += party_size * 20

print(f'{party_size} companions received {coins // party_size} coins each.')

