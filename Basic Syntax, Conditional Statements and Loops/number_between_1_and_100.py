MAX_NUMBER = 100
MIN_NUMBER = 1

while True:
    number = float(input())
    if MIN_NUMBER <= number <= MAX_NUMBER:
        print(f'The number {number} is between {MIN_NUMBER} and {MAX_NUMBER}')
        break
