with open('Python\\Advent-Of-Code\\2021\\Input\\Day3input.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

len = len(lines[0])
zerobit = [0 for _ in range(len)]
onebit = [0 for _ in range(len)]
for g in lines:
    for x in range(len):
        if g[x] == '0':
            zerobit[x] += 1
        else:
            onebit[x] += 1

# print(zerobit)
# print(onebit)

gammanum = ''
epsilonnum = ''
for one, zero in zip(onebit, zerobit):
    if one > zero:
        gammanum += '1'
        epsilonnum += '0'
    else:
        gammanum += '0'
        epsilonnum += '1'

print(int(gammanum, 2) * int(epsilonnum, 2))
