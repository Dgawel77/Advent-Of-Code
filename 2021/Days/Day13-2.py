with open('../Input/Day13input.txt') as f:
    lines = f.readlines()


def dotprint():
    minx, miny = 10000000000000, 10000000000000
    maxx, maxy = 0, 0
    for x, y in dots:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    for y in range(miny, maxy+1):
        print()
        for x in range(minx, maxx+1):
            if (x, y) in dots:
                print('█', end='')
            else:
                print(' ', end='')


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

for instruction in range(instructions, len(lines)):
    line = lines[instruction].strip()
    side = line[11]
    number = int(line[13:])
    fold(side, number)
dotprint()
