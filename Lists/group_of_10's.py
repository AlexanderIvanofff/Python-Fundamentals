from math import ceil

number_str = list(map(int, input().split(', ')))

max_value = max(number_str)
count_numbers = ceil(max_value / 10)

for i in range(1, count_numbers + 1):
    upper = i * 10
    lower = upper - 10
    res = [num for num in number_str if lower < num <= upper]
    print(f'Group of {i * 10}\'s: {res}')