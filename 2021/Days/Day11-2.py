with open('Python\\Advent-Of-Code\\2021\\Input\\Day11input.txt') as f:
    lines = list(map(lambda x: [int(c) for c in x], f.read().splitlines()))

flashed = set()


def flash(r, c):
    global flashed
    flashed.add((r, c))
    lines[r][c] = 0
    changes = [(1, 1), (1, 0), (1, -1), (0, 1),
               (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    for cr, cc in changes:
        nr, nb = r + cr, c + cc
        if 0 <= nr < len(lines) and 0 <= nb < len(lines[0]):
            if (nr, nb) not in flashed:
                lines[nr][nb] += 1
                if lines[nr][nb] >= 10 and not (nr, nb) in flashed:
                    flash(nr, nb)


def simulate():
    global flashed
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if (r, c) not in flashed:
                lines[r][c] += 1
                if lines[r][c] >= 10:
                    flash(r, c)
    octopi = len(lines) * len(lines[0])
    if octopi == len(flashed):
        return False
    return True


rounds = 1
while simulate():
    flashed.clear()
    rounds += 1
print(rounds)
