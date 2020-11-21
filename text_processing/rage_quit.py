line = input()

i = 0
current_str = ''
result = ''
while i < len(line):
    char = line[i]

    if char.isdigit():
        count_str = char

        if i + 1 < len(line) and line[i + 1].isdigit():
            count_str += line[i + 1]
            i += 1
        count = int(count_str)
        result += current_str.upper() * count
        current_str = ''
    else:
        current_str += char

    i += 1

print(f'Unique symbols used: {len(set(result))}')
print(result)