from typing import Counter

with open('Python\\Advent-Of-Code\\2021\\Input\\Day5input.txt') as f:
    lines = map(lambda x: x.strip(), f.readlines())

cnt = Counter()
for command in lines:
    first, second = command.split(' -> ')
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))
    stepx = 0 if x1 == x2 else 1 if x1 < x2 else -1
    stepy = 0 if y1 == y2 else 1 if y1 < y2 else -1
    while x1 != x2+stepx or y1 != y2+stepy:
        cnt[(x1, y1)] += 1
        x1 += stepx
        y1 += stepy


print(len([k for k, v in cnt.items() if v > 1]))
