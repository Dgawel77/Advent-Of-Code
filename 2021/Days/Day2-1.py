with open('Python\\Advent-Of-Code\\2021\\Input\\Day2input.txt') as f:
    lines = f.readlines()

h = 0
d = 0
for x in lines:
    n, m = x.split()
    if n == 'forward':
        h += int(m)
    elif n == 'down':
        d += int(m)
    elif n == 'up':
        d -= int(m)

print(d * h)
