with open('Python\\Advent-Of-Code\\2021\\Input\\Day10input.txt') as f:
    lines = f.read().split("\n")


score = 0
SyntaxScore = {')': 3, ']': 57, '}': 1197, '>': 25137}


def Corrupt(line):
    global score
    stack = []
    openings = set(['(', '<', '{', '['])
    otherSide = {')': '(', '>': '<', '}': '{', ']': '['}
    for c in line:
        if c in openings:
            stack.append(c)
        else:
            v = stack.pop()
            if otherSide[c] != v:
                score += SyntaxScore[c]
                break


for s in lines:
    Corrupt(s)

print(score)
