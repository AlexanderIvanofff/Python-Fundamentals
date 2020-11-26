skill = input()

command = input()

while not command == 'For Аzeroth':
    tokens = command.split()
    instruction = tokens[0]

    if instruction == 'GladiatorStance':
        skill = skill.upper()
        print(skill)

    elif instruction == 'DefenciveStance':
        skill = skill.lower()
        print(skill)

    elif instruction == 'Dispel':
        index = int(tokens[1])
        letter = tokens[2]

        if index in range(len(skill)):
            skill = list(skill)
            skill[index] = letter
            skill = "".join(skill)
            print('Success!')
        else:
            print(f'Dispel too weak.')

    elif instruction == 'Target':
        current_target_command = tokens[1]
        if current_target_command == 'Change':
            old_substring = tokens[2]
            current_substring = tokens[3]
            skill = skill.replace(old_substring, current_substring)
            print(skill)

        elif current_target_command == 'Remove':
            removed_substring = tokens[2]
            skill.replace(removed_substring, "")
            print(skill)
        else:
            print(f"Command doesn't exist!")
    else:
        print(f"Command doesn't exist!")

    command = input()