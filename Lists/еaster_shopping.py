shops = input().split()
n = int(input())

for index in range(n):
    tokens = input().split()
    instruction = tokens[0]

    if instruction == 'Include':
        shop = tokens[1]
        shops.append(shop)

    elif instruction == 'Visit':
        first_or_last = tokens[1]
        count = int(tokens[2])
        length = len(shops)

        if first_or_last == 'first':
            if count <= length:
                del shops[:count]

        elif first_or_last == 'last':
            if count <= length:
                del shops[len(shops) - count:]

    elif instruction == 'Prefer':
        first_index = int(tokens[1])
        second_index = int(tokens[2])

        if first_index in range(len(shops)) and second_index in range(len(shops)):
            shops[first_index], shops[second_index] = shops[second_index], shops[first_index]

    elif instruction == 'Place':
        first_shop = tokens[1]
        shop_index = int(tokens[2])

        if shop_index in range(len(shops)):
            shops.insert(shop_index + 1, first_shop)

print(f'Shops left:')
print(*shops)