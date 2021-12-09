def solve(rule, previous):
    if len(previous) > len(solveLine):
        return previous
    if rules[rule][0][0] in ['a', 'b']:
        return rules[rule][0][0]
    for string in rules[rule]:
        stringSoFar = ""
        for part in string:
            stringSoFar += solve(part, previous+stringSoFar)
        if previous+stringSoFar == solveLine[:len(previous+stringSoFar)]:
            return stringSoFar
    return stringSoFar

with open("Advent2020\Day19Input.txt") as f:
    lines = f.readlines()
rules = {}
for line in enumerate(lines):
    if line[1] == '\n':
        start = line[0]
        break
    split = line[1].split(' ', 1)
    rules[split[0][:-1]] = []
    for prerule in split[1][:-1].split(' | '):
        if prerule in [r'"a"', r'"b"']:
            prerule = prerule[1:-1]
        rules[split[0][:-1]].append(prerule.split(" "))

total = 0
for line in lines[start+1:]:
    global solveLine
    solveLine = line[:-1]
    if solveLine == solve('0', ""):
        total += 1
print(total)