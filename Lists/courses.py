def solve(number):
    total_courses = []
    for _ in range(number):
        courses = input()
        total_courses.append(courses)
    return total_courses


print(solve(int(input())))
