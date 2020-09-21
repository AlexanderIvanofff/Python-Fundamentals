DAYS_PER_YEAR = 365.2422


def centuries_to_minutes(centuries):
    years = centuries * 100
    days = int(years * DAYS_PER_YEAR)

    hours = days * 24
    minutes = hours * 60
    return f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes'


print(centuries_to_minutes(int(input())))