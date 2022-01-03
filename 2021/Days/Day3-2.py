with open('../Input/Day3input.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))


def mostCommon(list):
    length = len(list[0])
    zerobit = [0 for _ in range(length)]
    onebit = [0 for _ in range(length)]
    for g in list:
        for x in range(length):
            if g[x] == '0':
                zerobit[x] += 1
            else:
                onebit[x] += 1
    return (zerobit, onebit)


oxygenGenerator = [x for x in lines]
co2scrubing = [x for x in lines]
pos = 0
while len(oxygenGenerator) > 1:
    zerobit, onebit = mostCommon(oxygenGenerator)
    if onebit[pos] > zerobit[pos] or onebit[pos] == zerobit[pos]:
        oxygenGenerator = list(
            filter(lambda x: x[pos] == '1', oxygenGenerator))
    else:
        oxygenGenerator = list(
            filter(lambda x: x[pos] == '0', oxygenGenerator))
    pos += 1

pos = 0
while len(co2scrubing) > 1:
    zerobit, onebit = mostCommon(co2scrubing)
    if onebit[pos] > zerobit[pos] or onebit[pos] == zerobit[pos]:
        co2scrubing = list(filter(lambda x: x[pos] == '0', co2scrubing))
    else:
        co2scrubing = list(filter(lambda x: x[pos] == '1', co2scrubing))
    pos += 1

print(int(oxygenGenerator[0], 2) * int(co2scrubing[0], 2))
