def solve(password):
    messages = []
    valid_length = 6 <= len(password) <= 10
    are_letter_and_digit = password.isalnum()
    has_at_least_two_digits = len([x for x in password if x.isdigit()]) >= 2
    if valid_length and are_letter_and_digit and has_at_least_two_digits:
        messages.append('Password is valid')

    if not valid_length:
        messages.append('Password must be between 6 and 10 characters')
    if not are_letter_and_digit:
        messages.append('Password must consist only of letters and digits')
    if not has_at_least_two_digits:
        messages.append('Password must have at least 2 digits')

    return '\n'.join(messages)


print(solve(input()))