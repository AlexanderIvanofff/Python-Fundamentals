strings = input().split()

while True:
    command = input()
    if command == 'end':
        break
    tokens = command.split()

    instruction = tokens[0]
    if instruction == 'reverse':
        position = tokens[1]
        start = int(tokens[2])
        num = tokens[3]
        end = int(tokens[4])
        strings[start:start + end] = reversed(strings[start:end])

    elif instruction == 'sort':
        star = int(tokens[2])
        ends = int(tokens[4])
        strings[star:star + ends] = sorted(strings[star:star + ends])

    elif instruction == 'remove':
        count = int(tokens[1])
        del strings[:count]

print(', '.join(strings))