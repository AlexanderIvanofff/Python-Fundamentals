usernames = input().split(", ")


for username in usernames:
    if not (3 <= len(username) <= 16):
        continue

    is_valid = True
    for char in username:
        if not (char.isalnum() or char == '-' or char == '_'):
            is_valid = False
            break

    if not is_valid:
        continue

    print(username)
