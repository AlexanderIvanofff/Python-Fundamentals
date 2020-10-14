numbers = list(map(int, input().split()))


def exchange(nums_list, index):
    if 0 <= index < len(nums_list):
        fist_part = nums_list[:index + 1]
        second_part = nums_list[index + 1:]
        exchange_list = second_part + fist_part
        return exchange_list
    else:
        print(f'Invalid index')
        return nums_list


def get_max_odd(num_list):
    filter_list = list(filter(lambda x: x % 2 != 0, num_list))
    max_odd = max(filter_list)
    for i in range(len(num_list) - 1, -1, -1):
        if num_list[i] == max_odd:
            print(i)
            break
        else:
            print(f'No matches')


def get_max_even(num_list):
    filter_list = list(filter(lambda x: x % 2 != 1, num_list))
    max_even_num = max(filter_list)

    for i in range(len(max_even_num) - 1, -1, -1):
        if filter_list[i] == max_even_num:
            print(i)
            break
        else:
            print(f'No matches')


def get_min_even(num_list):
    filter_list = list(filter(lambda x: x % 2 != 1, num_list))
    min_even_number = min(filter_list)

    for i in range(len(num_list) - 1, -1, -1):
        if num_list[i] == min_even_number:
            print(i)
            break
        else:
            print(f'No matches')


def get_min_odd(num_list):
    filter_list = list(filter(lambda x: x % 2 != 0, num_list))
    min_odd_number = min(filter_list)

    for i in range(len(num_list) - 1, -1, -1):
        if num_list[i] == min_odd_number:
            print(i)
            break
        else:
            print(f'No matches')


def get_fist_two_odd_numbers(my_list, count):
    filter_list = list(filter(lambda x: x % 2 != 0, my_list))

    if count > len(filter_list):
        print(f'Invalid count')
    elif len(filter_list) == 0:
        print(f'[]')
    else:
        fist_two = filter_list[:2]
        print(fist_two)


def get_fist_two_even_element(my_list, count):
    filter_list = list(filter(lambda x: x % 2 == 0, my_list))

    if count > len(filter_list):
        print(f'Invalid count')
    elif len(filter_list) == 0:
        print(f'[]')
    else:
        fist_two = filter_list[:2]
        print(fist_two)


def get_last_two_odd_numbers(my_list, count):
    filter_list = list(filter(lambda x: x % 2 != 0, my_list))

    if count > len(filter_list):
        print(f'Invalid count')
    elif len(filter_list) == 0:
        print(f'[]')
    else:
        for i in range(len(filter_list)):
            print(filter_list[::-1])


def get_last_two_even_numbers(my_list, count):
    filter_list = list(filter(lambda x: x % 2 == 0, my_list))

    if count > len(filter_list):
        print(f'Invalid count')
    elif len(filter_list) == 0:
        print(f'[]')
    else:
        for i in range(len(filter_list)):
            print(filter_list[::-1])


while True:
    command = input()
    if command == 'end':
        break

    tokens = command.split()
    instruction = tokens[0]

    if instruction == 'exchange':
        data = int(tokens[1])
        numbers = exchange(numbers, data)

    elif instruction == 'max':
        data = tokens[1]

        if data == 'odd':
            get_max_odd(numbers)

        elif data == 'even':
            get_max_even(numbers)

    elif instruction == 'min':
        data = tokens[1]

        if data == 'odd':
            get_min_even(numbers)

        elif data == 'even':
            get_min_odd(numbers)

    elif instruction == 'fist':
        count = int(tokens[1])
        type_command = instruction[2]
        if type_command == 'odd':
            get_fist_two_odd_numbers(numbers, count)
        elif type_command == 'even':
            get_fist_two_even_element(numbers, count)

    elif instruction == 'last':
        count = int(tokens[1])
        type_command = instruction[2]

        if type_command == 'odd':
            get_last_two_odd_numbers(numbers, count)
        elif type_command == 'even':
            get_last_two_even_numbers(numbers, count)


print(f'{input().split()}')