import re

pattern = r"(U\$)([A-Za-z]{2,})\1(P@\$)([A-Za-z]{5,}[0-9]+)\3"
total_registration = 0
n = int(input())

for _ in range(n):
    registration = input()
    match = re.match(pattern, registration)

    if match is None:
        print("Invalid username or password")
        continue
    else:
        total_registration += 1
        print(f'Registration was successful')
        print(f'Username:{match.group(2)}, Password: {match.group(4)}')
print(f'Successful registration: {total_registration}')