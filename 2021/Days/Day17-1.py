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

for originalXVelocity in range(0, targetX[1]+1):
    for originalYVelocity in range(targetY[0], 1000):
        xVelocity, yVelocity = originalXVelocity, originalYVelocity
        xPosition, yPosition = 0, 0
        tmpYMax = 0
        for _ in range(1000):
            step()
            tmpYMax = max(tmpYMax, yPosition)
            if xPosition > targetX[1] or yPosition < targetY[0]:
                break
            if xPosition in xRange and yPosition in yRange:
                yMax = max(yMax, tmpYMax)
                #print("x:{} y:{} original: x {} y {} yMax {}".format(xPosition, yPosition, originalXVelocity, originalYVelocity, yMax))
                break
print(yMax)
