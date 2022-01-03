with open('../Input/Day9input.txt') as f:
    lines = f.read().split('\n')


totalRisk = 0
# find the low points
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
            totalRisk += int(lines[r][c]) + 1
print(totalRisk)
