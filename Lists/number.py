numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)

number = []
biggest_number = []
for i in range(len(numbers)):
    if numbers[i] > average:
        number.append(numbers[i])

for i in range(len(number)):
    if len(biggest_number) == 5:
        break
    biggest_number.append(max(number))
    number.remove(max(number))


print(*biggest_number)

if len(biggest_number) <= 0:
    print('No')
