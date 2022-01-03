from typing import Counter


with open('../Input/Day14input.txt') as f:
    lines = f.readlines()

start = lines[0].strip()

d = {}
for line in lines[2:]:
    poly = line.strip().split(' -> ')
    d[poly[0]] = poly[1]

for i in range(10):
    for x in range(0, 2*len(start)-2, 2):
        start = start[:x+1] + d[start[x:x+2]] + start[x+1:]

cnt = Counter(start)
print(cnt.most_common(1)[0][1] - cnt.most_common()[-1][1])
