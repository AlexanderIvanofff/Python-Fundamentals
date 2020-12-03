n = int(input())

total_piece = {}

for _ in range(n):
    piece, composer, key = input().split('|')

    total_piece[piece] = [composer, key]

command = input()
while not command == 'Stop':
    tokens = command.split('|')

    instructions = tokens[0]
    if instructions == 'Add':
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]

        if piece in total_piece:
            print(f'{piece} is already in the collection!')
        else:
            total_piece[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif instructions == 'Remove':
        piece = tokens[1]
        if piece in total_piece:
            del total_piece[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif instructions == 'ChangeKey':
        piece = tokens[1]
        new_key = tokens[2]

        if piece not in total_piece:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            total_piece[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')

    command = input()

for name, composer in sorted(total_piece.items(), key=lambda x: (x[0], x[1][0])):
    print(f'{name} -> Composer: {composer[0]}, Key: {composer[1]}')