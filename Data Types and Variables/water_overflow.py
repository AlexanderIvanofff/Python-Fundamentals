n = int(input())

TOTAL_CAPACITY = 255
total_liters = 0

for i in range(1, n + 1):
    liters = int(input())
    if total_liters + liters > TOTAL_CAPACITY:
        print(f'Insufficient capacity!')
    else:
        total_liters += liters

print(f'{total_liters}')
