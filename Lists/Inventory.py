items = input().split(', ')

input_command = input()
while input_command != 'Craft!':

    tokens = input_command.split(" - ")
    command = tokens[0]
    second_argument = tokens[1]

    if command == 'Collect':
        if second_argument not in items:
            items.append(second_argument)

    elif command == 'Drop':
        if second_argument in items:
            items.remove(second_argument)

    elif command == 'Combine Items':
        token = second_argument.split(':')
        old_item = token[0]
        new_item = token[1]

        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif command == 'Renew':
        if second_argument in items:
            items.remove(second_argument)
            items.append(second_argument)

    input_command = input()

print(', '.join(items))