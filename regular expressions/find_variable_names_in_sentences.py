import re

pattern = r'\b_([a-zA-Z0-9]+)\b'


def solve(text):
    matches = re.findall(pattern, text)
    return ",".join(matches)


print(solve(input()))