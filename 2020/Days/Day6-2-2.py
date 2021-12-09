with open("Advent2020\Day6Input.txt") as f:
    lines = f.read().split("\n")
common, remove, total= ["0"], [], 0
for line in lines:
    if common == ["0"]:
        common = []
        for char in line:
            common.append(char)
    else:
        if line == "":
            total += len(common)
            common = ["0"]
        else:
            for char in common:
                if char not in line:
                    remove.append(char)
            for char in remove:
                common.remove(char)
            remove=[]
print(total)
