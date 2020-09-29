def solve(number, search_word):
    total_strings = []
    strings_with_search_word = []
    for _ in range(number):
        current_strings = input()
        total_strings.append(current_strings)

        if search_word in current_strings:
            strings_with_search_word.append(current_strings)
    print(f'{total_strings}')
    print(f'{strings_with_search_word}')


solve(int(input()), input())