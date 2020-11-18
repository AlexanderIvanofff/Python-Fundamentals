def solve(text):
    for i in range(len(text)):
        if text[i] == ':':
            print(f':{text[i + 1]}')


solve(input())
