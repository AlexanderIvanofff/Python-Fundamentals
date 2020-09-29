def solve(number):
    negative = []
    positive = []
    for _ in range(number):
        num = int(input())
        if num <= 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
    print(positive)
    print(negative)
    return f'Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}'


print(solve(int(input())))