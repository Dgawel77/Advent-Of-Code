with open('../Input/Day11input.txt') as f:
    lines = list(map(lambda x: [int(c) for c in x], f.read().splitlines()))

flashed = set()
numflashes = 0

def flash(r, c):
    global flashed, numflashes
    flashed.add((r, c))
    numflashes += 1
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
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if (r, c) not in flashed:
                lines[r][c] += 1
                if lines[r][c] >= 10:
                    flash(r, c)

for x in range(0, 100):
    flashed.clear()
    simulate()
print(numflashes)
