with open('../Input/Day2input.txt') as f:
    lines = f.readlines()

h = 0
d = 0
a = 0
for x in lines:
    n, m = x.split()
    if n == 'forward':
        h += int(m)
        d += int(m) * a
    elif n == 'down':
        a += int(m)
    elif n == 'up':
        a -= int(m)

print(d * h)
