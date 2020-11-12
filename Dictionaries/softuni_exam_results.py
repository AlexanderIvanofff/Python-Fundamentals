from collections import defaultdict

command = input()

total_results = defaultdict(int)
total_languages = defaultdict(int)

while not command == 'exam finished':
    tokens = command.split('-')

    student_name = tokens[0]
    language = tokens[1]

    if language != 'banned':
        points = int(tokens[2])
        total_languages[language] += 1

        if points >= total_results[student_name]:
            total_results[student_name] = points
    else:
        del total_results[student_name]

    command = input()

sorted_result = dict(sorted(total_results.items(), key=lambda x: (-x[1], x[0])))

print(f'Results:')

for kay, value in sorted_result.items():
    print(f'{kay} | {value}')

print(f'Submissions:')

for k, v in sorted(total_languages.items()):
    print(f'{k} - {v}')