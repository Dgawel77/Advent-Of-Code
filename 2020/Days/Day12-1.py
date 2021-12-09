with open("Advent2020\Day12Input.txt") as f:
    lines = f.readlines()
X, Y, facing = 0, 0, 0
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
        facing = (facing + ammount)%360
    elif action == "R":
        facing = (facing - ammount)%360
    elif action == "F":
        if facing == 0:
            X += ammount
        elif facing == 90:
            Y += ammount
        elif facing == 180:
            X -= ammount
        elif facing == 270:
            Y -= ammount
print(abs(X) + abs(Y))