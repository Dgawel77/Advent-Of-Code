with open("Python\\Advent-Of-Code\\2015\\Input\\Day1Input.txt") as f:
    lines = f.read()
counter = 0
for char in lines:
    if char == ")":
        counter -= 1
    else:
        counter += 1
print(counter)