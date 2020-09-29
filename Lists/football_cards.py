cards = input().split()
team_a = [1] * 11
team_b = [1] * 11

for card in cards:
    token = card.split('-')

    team = token[0]
    player = int(token[1])

    if team == 'A':
        team_a[player - 1] = 0
    else:
        team_b[player - 1] = 0

print(f'Team A - {sum(team_a)}; Team B - {sum(team_b)}')

if team_a.count(1) < 7 or team_b.count(1) < 7:
    print(f'Game was terminated')