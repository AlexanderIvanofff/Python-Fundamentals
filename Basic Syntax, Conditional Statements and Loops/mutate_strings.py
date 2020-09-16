first_strings = input()
second_strings = input()

for i in range(len(first_strings)):
    if first_strings[i] != second_strings[i]:
        for second_string_index in range(0, i + 1):
            print(second_strings[second_string_index], end='')

        for first_string_index in range(i + 1, len(first_strings)):
            print(first_strings[first_string_index], end='')

        print()