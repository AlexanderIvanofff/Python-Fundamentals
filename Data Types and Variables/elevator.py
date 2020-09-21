import math


def solve(number_of_people, capacity):
    return math.ceil(number_of_people / capacity)


n = int(input())
p = int(input())

print(solve(n, p))

