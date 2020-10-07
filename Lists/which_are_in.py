def solve(words, second_string):
    return [n for n in words if n in second_string]


word = input().split(', ')
second_str = input()

print(solve(word, second_str))