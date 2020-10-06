notes = []

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split('-', maxsplit=1)
    priority = int(tokens[0])
    task = tokens[1]

    notes.append((priority, task))

sorted_tasks = [task_name for priority_task, task_name in sorted(notes)]

print(sorted_tasks)