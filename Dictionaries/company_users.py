from collections import defaultdict

command = input()
company_users = defaultdict(list)
while not command == 'End':
    tokens = command.split(' -> ')

    company_name = tokens[0]
    registration_number = tokens[1]

    if registration_number not in company_users[company_name]:
        company_users[company_name].append(registration_number)
    command = input()

sorted_dict = sorted(company_users.items(), key=lambda x: (x[0], x[1]))

for kay, employee in sorted_dict:
    print(kay)

    for name in employee:
        print(f'-- {name}')