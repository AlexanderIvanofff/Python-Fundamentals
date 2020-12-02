import re

n = int(input())
pattern = r"(.{1,})>([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<\1"

for _ in range(n):
    password = input()
    match = re.match(pattern, password)
    if match:
        current_password = match.group(2) + match.group(3)\
                           + match.group(4) + match.group(5)
        print(f'Password: {current_password}')
    else:
        print('Try another password!')