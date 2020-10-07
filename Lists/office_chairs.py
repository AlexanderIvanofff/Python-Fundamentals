n = int(input())

total_chairs = []
has_enough_space = True

for i in range(1, n + 1):
    tokens = input().split()
    chairs = len(tokens[0])
    count_chairs = int(tokens[1])

    if count_chairs <= chairs:
        current_chairs = chairs - count_chairs
        total_chairs.append(current_chairs)
    else:
        has_enough_space = False
        print(f'{abs(chairs - count_chairs)} more chairs needed in room {i}')

if has_enough_space:
    print(f'Game On, {sum(total_chairs)} free chairs left')