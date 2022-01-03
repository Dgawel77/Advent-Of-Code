from typing import Deque

with open('../Input/Day9input.txt') as f:
    lines = f.read().split('\n')


# find the basin size using a BFS
def basinSize(r, c):
    mark = set((r, c))
    queue = Deque()
    queue.append((r, c))
    size = 0
    while len(queue) != 0:
        lr, lc = queue.popleft()
        size += 1
        points = [(lr, lc-1), (lr, lc+1), (lr-1, lc), (lr+1, lc)]
        for nr, nc in points:
            if nr < 0 or nr >= len(lines) or nc < 0 or nc >= len(lines[r]):
                continue
            if lines[nr][nc] == '9':
                continue
            if lines[nr][nc] > lines[lr][lc] and (nr, nc) not in mark:
                mark.add((nr, nc))
                queue.append((nr, nc))
    return size


# find the low points
lowPoints = []
for r in range(len(lines)):
    for c in range(len(lines[r])):
        points = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
        valid = True
        for nr, nc in points:
            if nr < 0 or nr >= len(lines) or nc < 0 or nc >= len(lines[r]):
                continue
            if lines[nr][nc] <= lines[r][c]:
                valid = False
                break
        if valid:
            lowPoints.append((r, c))

sizes = []
for r, c in lowPoints:
    sizes.append(basinSize(r, c))

sizes = sorted(sizes)[-3:]
print(sizes[0] * sizes[1] * sizes[2])
