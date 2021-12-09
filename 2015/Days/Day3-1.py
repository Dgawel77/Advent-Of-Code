with open("Python\\Advent-Of-Code\\2015\\Input\\Day3Input.txt") as f:
    lines = f.read()
went, x, y, rx, ry= {}, 0, 0, 0, 0
went[(x, y)] = True
for char in enumerate(lines):
    if char[0] % 2 == 0:
        if char[1] == ">":
            x += 1
        elif char[1] == "<":
            x -= 1
        elif char[1] == "^":
            y += 1
        elif char[1] == "v":
            y -= 1
        went[(x, y)] = True
    else:    
        if char[1] == ">":
            rx += 1
        elif char[1] == "<":
            rx -= 1
        elif char[1] == "^":
            ry += 1
        elif char[1] == "v":
            ry -= 1
        went[(rx, ry)] = True
print(len(went))