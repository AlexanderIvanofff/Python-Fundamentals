old_version = input().split('.')
old_version = int(''.join(old_version))
new_version = str(old_version + 1)

print('.'.join(new_version))