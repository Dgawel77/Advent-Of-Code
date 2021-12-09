with open("Advent2020\Day5Input.txt") as f:
    lines = f.readlines()
largest = 0
for line in lines:
    power2, row = 6, 0
    for char in line[:-4]:
        if char == "B":
            row += 2**power2
        power2 -= 1
    power2, column = 2, 0
    for char in line[-4:-1]:
        if char == "R":
            column += 2**power2
        power2 -= 1
    if((row*8 + column) > largest):
        largest = (row*8 + column)
print(largest)
