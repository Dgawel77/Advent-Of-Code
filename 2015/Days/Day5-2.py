def pair():
    for x in range(0, len(line)-1):
        if line[x] == line [x+1]:
            if line[x:x+2] in line[x+2:]:
                print("hello")
                return True
    return False
def between():
    return False

with open("Python\\Advent-Of-Code\\2015\\Input\\Day5Input.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    print(pair())