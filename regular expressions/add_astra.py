import re

pattern = r"(#|\|)([A-Za-z ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]{1,10000})\1"
pattern_two = r"(#|\|)([A-Za-z ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]{1,10000})\1"

text = input()
match = re.finditer(pattern, text)
match_two = re.finditer(pattern, text)

total = 0

for index in match:
    total += int(index.group(4))

print(f'You have food to last you for: {total // 2000} days!')


for index in match_two:
    name = index.group(2)
    data = index.group(3)
    calories = index.group(4)

    print(f'Item: {name}, Best before: {data}, Nutrition: {calories}')