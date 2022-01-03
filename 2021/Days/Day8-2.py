from typing import Counter
with open('../Input/Day8input.txt') as f:
    lines = f.readlines()


def decode(digits):
    preset = [0, 0, 1, 7, 4, 0, 0, 8]
    known = ['' for _ in range(10)]
    for d in digits:
        known[preset[len(d)]] = d

    topsegment = set(known[7]).difference(set(known[1]))
    s = ['' for _ in range(8)]
    s[1] = list(topsegment)[0]
    cnt = Counter()
    for d in digits:
        for c in d:
            cnt[c] += 1

    for k, v in cnt.items():
        if v == 6:
            s[2] = k
        elif v == 4:
            s[5] = k
        elif v == 9:
            s[6] = k
    s[3] = known[1].replace(s[6], '', 1)
    s[4] = list(set(known[4]).difference(set([s[2], s[3], s[6]])))[0]
    s[7] = list(set(known[8]).difference(set(s[1:7])))[0]

    for d in digits:
        setd = set(d)
        if setd == set([s[1], s[2], s[3], s[5], s[6], s[7]]):
            known[0] = d
        elif setd == set([s[1], s[3], s[4], s[5], s[7]]):
            known[2] = d
        elif setd == set([s[1], s[3], s[4], s[6], s[7]]):
            known[3] = d
        elif setd == set([s[1], s[2], s[4], s[6], s[7]]):
            known[5] = d
        elif setd == set([s[1], s[2], s[4], s[5], s[6], s[7]]):
            known[6] = d
        elif setd == set([s[1], s[2], s[3], s[4], s[6], s[7]]):
            known[9] = d

    return known


total = 0
for line in lines:
    signal, output = line.strip().split(' | ')
    output = output.split()
    signal = signal.split()
    decoder = decode(signal)
    num = ''
    for o in output:
        for n in range(0, 10):
            if set(o) == set(decoder[n]):
                num += str(n)
    total += int(num)

print(total)
