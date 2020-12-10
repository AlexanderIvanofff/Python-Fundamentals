"""
Create a program that manages messages sent and received of users. You need to keep information about username,
their sent and received messages. You will receive the capacity of possible messages kept at once per user.
You will be receiving lines with commands until you receive the "Statistics" command.  There are three possible commands:

"Add={username}={sent}={received}":
Add the username, his/her sent and received messages to your records. If person with the given username already exists
ignore the line.
"Message={sender}={receiver}":
Check if both usernames exist and if they do, increase the sender’s sent messages by 1 and the receiver’s received
messages by 1. If anyone reaches the capacity (first check the sender), he/she should be removed from the record and you
should print the following message:
"{username} reached the capacity!"
"Empty={username}":
Delete all records of the given user, if he exists. If "All" is given as username - delete all records you have.
In the end, you have to print the count of users, each person with his/her messages (the count of both sent and received)
sorted in descending order by the received messages and then by their username in ascending order in the following format:

Users count: {count}

{username} - {messages}

{username} - {messages}

"""


def add(username_dict, current_name, current_sent, current_received):
    if current_name not in username_dict:
        username_dict[current_name] = {"send": current_sent, "received": current_received}
    return username_dict


def message(username_dict, current_sender, current_receiver):
    if current_sender in username_dict and current_receiver in username_dict:
        username_dict[current_sender]["send"] += 1
        username_dict[current_receiver]["received"] += 1
    if username_dict[current_sender]["send"] + username_dict[current_sender]["received"] >= capacity:
        del username_dict[current_sender]
        print(f'{current_sender} reached the capacity!')
    if username_dict[current_receiver]["received"] + username_dict[current_receiver]["send"] >= capacity:
        del username_dict[current_receiver]
        print(f'{current_receiver} reached the capacity!')
    return username_dict


def empty(username_dict, current_username):
    if current_username in username_dict:
        del username_dict[current_username]
    elif current_username == 'All':
        username_dict.clear()
    return username_dict


capacity = int(input())
username_info = {}

command = input()

while not command == 'Statistics':
    tokens = command.split('=')
    instructions = tokens[0]
    if instructions == 'Add':
        person_name = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])

        username_info = add(username_info, person_name, sent, received)

    elif instructions == 'Message':
        sender = tokens[1]
        receiver = tokens[2]

        username_info = message(username_info, sender, receiver)

    elif instructions == 'Empty':
        username = tokens[1]

        username_info = empty(username_info, username)
    command = input()

print(f'Users count: {len(username_info)}')

for kay, value in sorted(username_info.items(), key=lambda x: (-x[1]["received"], x[0])):
    result = value["received"] + value["send"]
    print(f'{kay} - {result}')