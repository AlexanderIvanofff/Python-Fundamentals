def drive(car_dict, current_car, current_distance, current_fuel):
    if car_dict[current_car]["fuel"] < current_fuel:
        print(f'Not enough fuel to make that ride')
    else:
        car_dict[current_car]["fuel"] -= current_fuel
        car_dict[current_car]["mileage"] += current_distance
        print(f'{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.')
    if car_dict[current_car]["mileage"] >= 100_000:
        del car_dict[current_car]
        print(f'Time to sell the {current_car}!')
    return car_dict


def refuel(car_dict, current_car, current_ref):
    if car_dict[current_car]['fuel'] + current_ref < 75:
        car_dict[current_car]['fuel'] += current_ref
        print(f'{current_car} refueled with {current_ref} liters')
    else:
        left = 75 - car_dict[current_car]['fuel']
        print(f'{current_car} refueled with {left} liters')
        car_dict[current_car]['fuel'] = 75
    return car_dict


def revert(car_dict, current_car, current_kilometers):
    if car_dict[current_car]["mileage"] - current_kilometers < 10_000:
        car_dict[current_car]["mileage"] = 10000
    else:
        car_dict[current_car]["mileage"] -= current_kilometers
        print(f'{current_car} mileage decreased by {current_kilometers} kilometers')
    return car_dict


n = int(input())

total_car = {}
for _ in range(n):
    car_name, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)

    total_car[car_name] = {"mileage": mileage, 'fuel': fuel}


command = input()

while not command == 'Stop':
    tokens = command.split(' : ')
    instructions = tokens[0]

    if instructions == 'Drive':
        car = tokens[1]
        distance = int(tokens[2])
        fuel = int(tokens[3])
        total_car = drive(total_car, car, distance, fuel)

    elif instructions == 'Refuel':
        car = tokens[1]
        ref = int(tokens[2])

        total_car = refuel(total_car, car, ref)

    elif instructions == 'Revert':
        car = tokens[1]
        kilometers = int(tokens[2])
        total_car = revert(total_car, car, kilometers)

    command = input()

for kay, value in sorted(total_car.items(), key=lambda x: (-x[1]["mileage"], x[0])):
    print(f'{kay} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')
