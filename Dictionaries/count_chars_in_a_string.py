from collections import defaultdict


def solve(string):
    count_strings = defaultdict(int)
    for ch in string:
        if ch == ' ':
            continue
        count_strings[ch] += 1

    for kay, item in count_strings.items():
        print(f'{kay} -> {item}')


solve(input())