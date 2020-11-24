import re


def solve(text, search_word):
    pattern = rf"\b{search_word}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)


print(solve(input(), input()))