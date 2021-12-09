with open("Python\\Advent-Of-Code\\2015\\Input\\Day1Input.txt") as f:
    lines = f.read()
counter = 0
for char in enumerate(lines):
    if counter < 0:
        print(char[0]+1)
        break
    if char[1] == ")":
        counter -= 1
    else:
        counter += 1
print(counter)