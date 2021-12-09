with open("Advent2020\Day12Input.txt") as f:
    lines = f.readlines()
X, Y, sX, sY = 10, 1, 0, 0
for line in lines:
    action = line[0]
    ammount = int(line[1:])
    if action == "N":
        Y += ammount
    elif action == "S":
        Y -= ammount
    elif action == "E":
        X += ammount
    elif action == "W":
        X -= ammount
    elif action == "L":
        if ammount == 90:
            X, Y = -Y, X
        elif ammount == 180:
            X, Y = -X, -Y
        elif ammount == 270:
            X, Y = Y, -X
    elif action == "R":
        if ammount == 90:
            X, Y = Y, -X
        elif ammount == 180:
            X, Y = -X, -Y
        elif ammount == 270:
            X, Y = -Y, X
    elif action == "F":
        for _ in range(0, ammount):
            sX += X
            sY += Y
#print(X)
#print(Y)
#print(sX)
#print(sY)
print(abs(sX) + abs(sY))