number = int(input())

total_sum = 0
for char in range(number):
    chars = input()
    total_sum += ord(chars)

print(f'The sum equals: {total_sum}')