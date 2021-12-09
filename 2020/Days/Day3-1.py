with open("Python\\Advent2020\\Advent-Of-Code-2020\\Input\\Day3Input.txt", "r") as f:
    lines = f.readlines()

position, TreesHit = 0, 0
for line in lines:
    if line[position] == "#":
        TreesHit += 1
    position = (position + 3) % 31
print(TreesHit)
