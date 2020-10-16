products = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break

    tokens = command.split()
    instructions = tokens[0]

    if instructions == 'Urgent':
        items = tokens[1]

        if items in products:
            continue
        else:
            products.insert(0, items)

    elif instructions == 'Unnecessary':
        items = tokens[1]
        if items in products:
            products.remove(items)
        else:
            continue

    elif instructions == 'Correct':
        old_item = tokens[1]
        new_item = tokens[2]
        for index in range(len(products)):
            if products[index] == old_item:
                products.pop(index)
                products.insert(index, new_item)

    elif instructions == 'Rearrange':
        items = tokens[1]
        for index in range(len(products)):
            if products[index] == items:
                products.pop(index)
                products.append(items)


print(f'{", ".join(products)}')