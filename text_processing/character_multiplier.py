text = input().split(' ')

first_string = text[0]
second_string = text[1]

min_length = min(len(first_string), len(second_string))

total_sum = 0
for i in range(min_length):
    res = ord(first_string[i]) * ord(second_string[i])
    total_sum += res

biggest_word = first_string

if len(second_string) > len(first_string):
    biggest_word = second_string

for i in range(min_length, len(biggest_word)):
    total_sum += ord(biggest_word[i])

print(total_sum)