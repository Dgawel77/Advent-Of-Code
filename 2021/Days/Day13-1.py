with open('Python\\Advent-Of-Code\\2021\\Input\\Day13input.txt') as f:
    lines = f.readlines()


def fold(side, number):
    global dots
    addition = set()
    subtraction = set()
    if side == 'y':
        for x, y in dots:
            if y > number:
                ny = number + (number - y)
                subtraction.add((x, y))
                addition.add((x, ny))

    else:
        for x, y in dots:
            if x > number:
                nx = number + (number - x)
                subtraction.add((x, y))
                addition.add((nx, y))

    dots = dots.difference(subtraction)
    dots = dots.union(addition)


dots = set()
for x in range(len(lines)):
    line = lines[x]
    if line == '\n':
        instructions = x + 1
        break
    s = line.strip().split(',')
    dots.add((int(s[0]), int(s[1])))

for instruction in range(instructions, instructions + 1):
    line = lines[instruction].strip()
    side = line[11]
    number = int(line[13:])
    fold(side, number)

print(len(dots))
