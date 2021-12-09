with open('Python\\Advent-Of-Code\\2021\\Input\\Day1input.txt') as f:
    lines = list(map(int, f.readlines()))

c = 0
for p in range(3, len(lines)):
    if (sum(lines[p-3:p]) < sum(lines[p-2:p+1])):
        c += 1

print(c)
