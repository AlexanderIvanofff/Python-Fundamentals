n_people = int(input())
lift = list(map(int, input().split()))

MAX_SEATS_PER_WAGON = 4

for index in range(len(lift)):
    while not lift[index] == MAX_SEATS_PER_WAGON:
        if n_people > 0:
            lift[index] += 1
            n_people -= 1
        else:
            break

all_seats = len(lift) * MAX_SEATS_PER_WAGON
taken_seats = sum(lift)

if n_people == 0 and taken_seats < all_seats:
    print(f'The lift has empty spots!')

elif n_people > 0 and taken_seats == all_seats:
    print(f'There isn\'t enough space! {n_people} people in a queue!')

print(' '.join([str(x) for x in lift]))