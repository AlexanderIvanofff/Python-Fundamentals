from collections import defaultdict

command = input()
courses = defaultdict(list)

while command != 'end':
    tokens = command.split(' : ')
    programing_name = tokens[0]
    student_name = tokens[1]

    courses[programing_name].append(student_name)
    command = input()

sorted_dict = dict(sorted(courses.items(), key=lambda name: -len(name[1])))

for k, v in sorted_dict.items():
    print(f'{k}: {len(v)}')

    for user_names in sorted(v):
        print(f'-- {user_names}')
