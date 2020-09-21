METERS_IN_KILOMETERS = 1000


def solve(meters):
    return meters / METERS_IN_KILOMETERS


print(f'{solve(int(input())):.2f}')