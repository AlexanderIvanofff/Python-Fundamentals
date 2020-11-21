def get_letter_position_in_alphabet(letter):
    position = ord(letter) - 96

    if letter.isupper():
        position = ord(letter) - 64

    return position


def calculate_item_result(line):
    first_element = line[0]
    last_element = line[-1]
    number = int(line[1: -1])

    first_letter_position_letter = get_letter_position_in_alphabet(first_element)
    last_letter_position_letter = get_letter_position_in_alphabet(last_element)

    result = 0

    if first_element.isupper():
        result = number / first_letter_position_letter
    else:
        result = number * first_letter_position_letter

    if last_element.isupper():
        result -= last_letter_position_letter
    else:
        result += last_letter_position_letter

    return result


items = input().split()
total_sum = 0

for item in items:
    res = calculate_item_result(item)
    total_sum += res

print(f'{total_sum:.2f}')
