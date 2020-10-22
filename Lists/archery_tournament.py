targets = [int(target) for target in input().split("|")]
points = 0
while True:
    line = input()
    if line == "Reverse":
        targets.reverse()
        continue
    elif line == "Game over":
        break

    line = line.split(" ")
    traversing = line[1].split("@")
    direction = traversing[0]
    start = int(traversing[1])
    length = int(traversing[2])

    if start in range(len(targets)):
        if direction == "Left":
            index = start - length
            if index < 0:
                while index < 0:
                    index += len(targets)
        else:
            index = start + length
            if index >= len(targets):
                while index >= len(targets):
                    index -= len(targets)

        if targets[index] >= 5:
            points += 5
            targets[index] -= 5
        else:
            points += targets[index]
            targets[index] = 0


print(f"{' - '.join([str(target) for target in targets])}")
print(f"Iskren finished the archery tournament with {points} points!")
