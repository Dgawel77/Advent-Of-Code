with open('Python\\Advent-Of-Code\\2021\\Input\\Day10input.txt') as f:
    lines = f.read().split("\n")


scores = []


def Validation(line):
    global scores
    stack = []
    openings = set(['(', '<', '{', '['])
    otherSide = {'(': ')', '<': '>', '{': '}', '[': ']'}
    for c in line:
        if c in openings:
            stack.append(c)
        else:
            stack.pop()
    additions = []
    for c in stack[::-1]:
        additions.append(otherSide[c])

    score = 0
    characterScore = {')': 1, '}': 3, ']': 2, '>': 4}
    for c in additions:
        score *= 5
        score += characterScore[c]
    scores.append(score)


def isCorrupt(line):
    stack = []
    openings = set(['(', '<', '{', '['])
    otherSide = {')': '(', '>': '<', '}': '{', ']': '['}
    for c in line:
        if c in openings:
            stack.append(c)
        else:
            v = stack.pop()
            if otherSide[c] != v:
                return True
    return False


remove = []
for s in lines:
    if isCorrupt(s):
        remove.append(s)

for r in remove:
    lines.remove(r)

for s in lines:
    Validation(s)

print(sorted(scores)[len(scores) // 2])
