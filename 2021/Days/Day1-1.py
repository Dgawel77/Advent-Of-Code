with open('../Input/Day1input.txt') as f:
    lines = list(map(int, f.readlines()))

c = 0
for p in range(0, len(lines)):
    if lines[p] > lines[p-1]:
        c += 1

print(c)
