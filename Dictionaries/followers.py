def new_follower(name_information_dict, current_username):
    if current_username not in name_information_dict:
        name_information_dict[current_username] = {'like': 0, 'comments': 0}
    return name_information_dict


def like(name_information_dict, current_username, current_count):
    if current_username in name_information_dict:
        name_information_dict[current_username]['like'] += current_count
    else:
        name_information_dict[current_username] = {"like": current_count, 'comments': 0}
    return name_information_dict


def comment(name_information_dict, current_username):
    if current_username not in name_information_dict:
        name_information_dict[current_username] = {"like": 0, 'comments': 1}
    else:
        name_information_dict[current_username]["comments"] += 1
    return name_information_dict


def blocked(name_information_dict, current_username):
    if current_username in name_information_dict:
        del name_information_dict[current_username]
    else:
        print(f'{current_username} doesn\'t exist.')
    return name_information_dict


name_information = {}

command = input()

while not command == 'Log out':
    tokens = command.split(": ")
    instructions = tokens[0]

    if instructions == 'New follower':
        username = tokens[1]

        name_information = new_follower(name_information, username)

    elif instructions == 'Like':
        username = tokens[1]
        count = int(tokens[2])

        name_information = like(name_information, username, count)

    elif instructions == 'Comment':
        username = tokens[1]
        name_information = comment(name_information, username)

    elif instructions == 'Blocked':
        username = tokens[1]
        name_information = blocked(name_information, username)

    command = input()


print(f'{len(name_information)} followers')

for kay, value in sorted(name_information.items(), key=lambda x: (-x[1]['like'] + x[1]["comments"], x[0])):
    total_likes_and_commends = value["like"] + value["comments"]
    print(f'{kay}: {total_likes_and_commends}')
