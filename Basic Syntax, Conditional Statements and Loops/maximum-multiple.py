def solution(first_number, second_number):
    numbers = 0
    for i in range(second_number, 0, -1):
        if i % first_number == 0:
            numbers += i
            break
    return numbers


print(solution(int(input()), int(input())))