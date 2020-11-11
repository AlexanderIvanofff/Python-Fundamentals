from collections import defaultdict

n = int(input())

total_score_and_students_name = defaultdict(list)
for i in range(n):
    student_name = input()
    score = float(input())
    total_score_and_students_name[student_name].append(score)

average_grade = {}
for kay, value in total_score_and_students_name.items():
    average_score = sum(value) / len(value)
    average_grade[kay] = average_score

    if average_score < 4.5:
        average_grade.popitem()


sorted_dict = dict(sorted(average_grade.items(), key=lambda x: -x[1]))

for i, k in sorted_dict.items():
    print(f'{i} -> {k:.2f}')