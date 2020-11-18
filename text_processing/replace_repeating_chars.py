string = list(input())

fixed_string = [v for i, v in enumerate(string) if i == 0 or v != string[i-1]]

print(''.join(fixed_string))
