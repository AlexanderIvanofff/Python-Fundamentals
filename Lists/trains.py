def solve(count_wagons):
    wagons = [0] * count_wagons

    while True:
        command = input()
        if command == 'End':
            break

        tokens = command.split(' ')
        instruction = tokens[0]

        if instruction == 'add':
            count = int(tokens[1])
            wagons[-1] += count

        elif instruction == 'insert':
            index = int(tokens[1])
            count = int(tokens[2])
            wagons[index] += count

        elif instruction == 'leave':
            index = int(tokens[1])
            count = int(tokens[2])
            wagons[index] -= count

    return wagons


print(solve(int(input())))