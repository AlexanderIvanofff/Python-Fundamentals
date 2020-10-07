def solve(electrons):
    result = []
    shield_index = 1
    while electrons > 0:
        value = 2 * pow(shield_index, 2)

        if electrons < value:
            result.append(electrons)
        else:
            result.append(value)

        electrons -= value
        shield_index += 1

    return result


print(solve(int(input())))