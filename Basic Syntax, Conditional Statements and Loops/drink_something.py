def under_14(years):
    if years <= 14:
        return f'drink toddy'


def under_18(years):
    if years <= 18:
        return f'drink coke'


def under_21(years):
    if years <= 21:
        return f'drink beer'


def above_21(years):
    if years > 21:
        return f'drink whisky'


def solve(years):
    if years <= 14:
        return under_14(years)
    elif years <= 18:
        return under_18(years)
    elif years <= 21:
        return under_21(years)
    elif years > 21:
        return above_21(years)


print(solve(int(input())))