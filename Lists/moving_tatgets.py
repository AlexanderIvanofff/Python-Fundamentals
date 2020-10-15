target = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split()

    instructions = tokens[0]
    index = int(tokens[1])
    value = int(tokens[2])

    if instructions == 'Shoot':
        if 0 <= index < len(target):
            target[index] -= value
            if target[index] <= 0:
                target.pop(index)

    elif instructions == 'Add':
        if 0 <= index < len(target):
            target.insert(index, value)
        else:
            print(f'Invalid placement!')

    elif instructions == 'Strike':
        start = index - value
        end = index + value

        if start >= 0 and end < len(target):
            del target[start:end + 1]
        else:
            print(f'Strike missed!')

target = [str(x) for x in target]
print('|'.join(target))