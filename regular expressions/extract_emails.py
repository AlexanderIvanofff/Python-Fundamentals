import re

user_pattern = r"( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"


def solve(text):
    pattern = rf"{user_pattern}@{host_pattern}"
    mails = re.finditer(pattern, text)

    for mail in mails:
        print(mail[0])


solve(input())