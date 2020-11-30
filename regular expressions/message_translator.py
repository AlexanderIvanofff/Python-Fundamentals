import re

pattern = r"!([A-Z]{1}[a-z]{3,})!:\[([A-Z-a-z]{8,})\]"

n = int(input())

for _ in range(n):
    message = input()

    match = re.match(pattern, message)
    if match is None:
        print('The message is invalid')
    else:
        command = match[1]
        message = match[2]
        print(f'{command}:', end=' ')
        for char in message:
            print(f'{ord(char)}', end=' ')
        print()