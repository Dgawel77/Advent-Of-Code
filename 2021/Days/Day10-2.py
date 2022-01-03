with open('../Input/Day10input.txt') as f:
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
    
    stack = list(map(lambda x: otherSide[x], stack))

    score = 0
    characterScore = {')': 1, ']': 2, '}': 3, '>': 4}
    for c in stack[::-1]:
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


lines = filter(lambda x: not isCorrupt(x), lines)

for s in lines:
    Validation(s)

print(sorted(scores)[len(scores) // 2])
