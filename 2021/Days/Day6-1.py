with open('../Input/Day6input.txt') as f:
    lines = list(map(int, f.read().split(',')))

for d in range(0, 80):
    # print(d)
    for p in range(0, len(lines)):
        lines[p] -= 1
        if lines[p] == -1:
            lines[p] = 6
            lines.append(8)

print(len(lines))
