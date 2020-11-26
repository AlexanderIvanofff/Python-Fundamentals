import re

pattern = r"^(\$|\%)([A-Z][a-z]{3, })\1:[ ]\[(\d+)\|\[(\d+)\]\|\[(d\+)\]\|$"

n = int(input())

for _ in range(n):
    message = input()
    match = re.fullmatch(pattern, message)

    if match:
        tag = match.group(2)
        message_to_deg = message.split(": ")[1].split('|')
        message_to_deg.pop()
        message = "".join([chr(int(x[1:-1])) for x in message_to_deg])
        print(f'{tag}: {message}')

    else:
        print(f'Valid message not found!')
