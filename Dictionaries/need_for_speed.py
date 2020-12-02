n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]


commands = input()

while not commands == 'Stop':
    tokens = commands.split(' : ')

    instructions = tokens[0]
    car = tokens[1]

    if instructions == 'Drive':
        distance = int(tokens[2])
        fuel = int(tokens[3])

        if cars[car][1] <= fuel:
            print(f'Not enough fuel to make that ride')
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if cars[car][0] >= 100_000:
            print(f'Time to sell the {car}!')
            del cars[car]

    elif instructions == 'Refuel':
        fuel = int(tokens[2])
        if cars[car][1] + fuel > 75:
            print(f'{car} refueled with {75 - cars[car][1] } liters')
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
            print(f'{car} refueled with {fuel} liters')

    elif instructions == 'Revert':
        kilometers = int(tokens[2])

        if cars[car][0] - kilometers < 10_000:
            cars[car][0] = 10_000
        else:
            cars[car][0] -= kilometers
            print(f'{car} mileage decreased by {kilometers} kilometers')

    commands = input()

for kay, value in sorted(cars.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{kay} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
