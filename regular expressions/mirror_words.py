import re

pattern = r"(#|@)([a-zA-z]{3,})\1{2}([a-zA-Z]{3,})\1"


string = input()
matches = re.finditer(pattern, string)

full_mach = []
mirrors = []

for mach in matches:
    full_mach.append(mach[0])
    if mach.group(2) == mach.group(3)[::-1]:
        full_maching = mach.group(2) + ' ' + '<=>' + ' ' + mach.group(3)
        mirrors.append(full_maching)

if len(full_mach) <= 0:
    print(f'No word pairs found!')
else:
    print(f'{len(full_mach)} word pairs found!')

if len(mirrors) <= 0:
    print('No mirror words!')
else:
    print(f'The mirror words are:')
    print(', '.join([x for x in mirrors]))