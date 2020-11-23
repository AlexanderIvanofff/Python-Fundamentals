import re

pattern = "\d+"
while True:
    string = input()

    if not string:
        break

    matches = re.findall(pattern, string)
    for match in matches:
        print(match, end=' ')