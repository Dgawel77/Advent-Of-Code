# Disclaimer this solution is very slow and just brute forces it
# hoping that the solutions are have a maximum velocity of 999
# also that the hits occure before 1000 steps.
# to make it faster I would use some kind of memoized table
# or use dynamic programming
with open('../Input/Day17input.txt') as f:
    lines = f.readlines()


def step():
    global xPosition, yPosition, xVelocity, yVelocity
    xPosition += xVelocity
    yPosition += yVelocity
    if xVelocity > 0:
        xVelocity += -1
    elif xVelocity < 0:
        xVelocity += 1
    yVelocity += -1


xPosition, yPosition = 0, 0
xVelocity, yVelocity = 0, 0
yMax = 0
targetLine = lines[0].split(', ')
targetX = tuple(map(int, targetLine[0][15:].split('..')))
targetY = tuple(map(int, targetLine[1][2:].split('..')))
xRange = range(targetX[0], targetX[1] + 1)
yRange = range(targetY[0], targetY[1] + 1)
hits = set()

for originalXVelocity in range(0, targetX[1]+1):
    for originalYVelocity in range(targetY[0], 1000):
        xVelocity, yVelocity = originalXVelocity, originalYVelocity
        xPosition, yPosition = 0, 0
        for _ in range(1000):
            step()
            if xPosition > targetX[1] or yPosition < targetY[0]:
                break
            if xPosition in xRange and yPosition in yRange:
                hits.add((originalXVelocity, originalYVelocity))
                break
print(len(hits))
