command = input()
followers = {}
while not command == 'Log out':
    tokens = command.split(': ')
    instructions = tokens[0]
    username = tokens[1]

    if instructions == 'New follower':
        if username not in followers:
            followers[username] = [0, 0]

    elif instructions == 'Like':
        count = int(tokens[2])
        if username in followers:
            followers[username][0] += count
        else:
            followers[username] = [count, 0]

    elif instructions == 'Comment':
        if username in followers:
            followers[username][1] += 1
        else:
            followers[username] = [0, 1]

    elif instructions == 'Blocked':
        if username in followers:
            del followers[username]
        else:
            print(f'{username} doesn\'t exist')

    command = input()
print(f'{len(followers)} followers')
for kay, value in sorted(followers.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{kay}: {sum(value)}')