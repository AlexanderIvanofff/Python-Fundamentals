def add(piece_dict, current_piece, current_composer, current_key):
    if current_piece in piece_dict:
        print(f'{current_piece} is already in the collection!')
    else:
        piece_dict[current_piece] = {'composer': current_composer, 'key': current_key}
        print(f'{current_piece} by {current_composer} in {current_key} added to the collection!')
    return piece_dict


def remove(dict_piece, current_piece):
    if current_piece in dict_piece:
        del dict_piece[current_piece]
        print(f'Successfully removed {current_piece}!')
    else:
        print(f'Invalid operation! {current_piece} does not exist in the collection.')
    return dict_piece


def change_key(piece_dict, current_piece, current_new_key):
    if current_piece in piece_dict:
        piece_dict[current_piece]["key"] = current_new_key
        print(f'Changed the key of {current_piece} to {current_new_key}!')
    else:
        print(f'Invalid operation! {current_piece} does not exist in the collection.')
    return piece_dict


n = int(input())

total_piece = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    total_piece[piece] = {'composer': composer, 'key': key}


command = input()

while not command == 'Stop':
    tokens = command.split('|')
    instructions = tokens[0]

    if instructions == 'Add':
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]

        total_piece = add(total_piece, piece, composer, key)

    elif instructions == 'Remove':
        piece = tokens[1]

        total_piece = remove(total_piece, piece)

    elif instructions == 'ChangeKey':
        piece = tokens[1]
        new_key = tokens[2]

        total_piece = change_key(total_piece, piece, new_key)

    command = input()


for kay, value in sorted(total_piece.items(), key=lambda x: (x[0], x[1]["composer"])):
    print(f'{kay} -> Composer: {value["composer"]}, Key: {value["key"]}')
