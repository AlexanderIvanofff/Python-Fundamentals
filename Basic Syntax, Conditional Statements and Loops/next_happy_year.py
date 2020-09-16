year = input()
year_int = int(year) + 1
year_str = str(year_int)

while True:
    symbols_count = len(year)
    unique_count = len(set(year))

    if symbols_count == unique_count:
        break
    else:
        year_int += 1
        year = str(year_int)

print(year)