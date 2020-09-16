desired_size = int(input())
direction = 1
current_size = 0

while (current_size < desired_size and direction == 1) or (direction == -1 and current_size > 0):
    current_size += direction
    print('*' * current_size)

    if desired_size == current_size:
        direction = -1