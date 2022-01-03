with open('../Input/Day6input.txt') as f:
    lines = list(map(int, f.read().split(',')))

numFish = [0 for _ in range(0, 9)]
for f in lines:
    numFish[f] += 1

for d in range(0, 256):
    tmp = [0 for _ in range(0, 9)]
    tmp[8] += numFish[0]
    tmp[6] += numFish[0]
    for s in range(1, 9):
        tmp[s-1] += numFish[s]
    numFish = tmp

print(sum(numFish))
