from typing import Counter

with open('Python\\Advent-Of-Code\\2021\\Input\\Day14input.txt') as f:
    lines = f.readlines()

start = lines[0].strip()

d = {}
for line in lines[2:]:
    poly = line.strip().split(' -> ')
    d[poly[0]] = poly[1]

cnt = Counter()
for i in range(0, len(start)-1):
    cnt[start[i:i+2]] += 1

for i in range(40):
    newCnt = Counter()
    for k, v in cnt.items():
        letter = d[k]
        newCnt[k[0] + d[k]] += v
        newCnt[d[k] + k[1]] += v
    cnt = newCnt

letterCount = Counter()
for k, v in cnt.items():
    letterCount[k[1]] += v
letterPair, count = next(iter(cnt.items()))
letterCount[letterPair[0]] += count

print(letterCount.most_common(1)[0][1] - letterCount.most_common()[-1][1])
