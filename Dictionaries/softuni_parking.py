n = int(input())
parking = {}

for _ in range(n):
    arcs = input().split()
    command = arcs[0]
    username = arcs[1]

    if command == 'register':
        licensePlateNumber = arcs[2]

        if username in parking:
            print(f'ERROR: already registered with plate number {parking[username]}')
            continue

        parking[username] = licensePlateNumber
        print(f'{username} registered {licensePlateNumber} successfully')

    elif command == 'unregister':
        if username not in parking:
            print(f'ERROR: user {username} not found')
            continue

        parking.pop(username)
        print(f'{username} unregistered successfully')


for kay, value in parking.items():
    print(f'{kay} => {value}')