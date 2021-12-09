with open("Advent2020\Day6Input.txt") as f:
    lines = f.read().split("\n")
total,common, samecounter, numquestions = 0, [], 0, 0
for line in lines:
    if line != "":
        for char in line:
            common.append(char)
        numquestions += 1
    else:
        common.sort()
        common.append("0")
        for x in range(1, len(common)):
            if common[x-1] == common[x]:
                samecounter+= 1
            else:
                if samecounter == numquestions-1:
                    total+= 1
                samecounter = 0
        common, numquestions = [], 0
print(total)