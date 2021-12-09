with open("Day6Input.txt") as f:
    lines = f.read().split("\n")
total, charachters= 0, []
for line in lines:
    if line == "":
        total += len(charachters)
        charachters = []
    for char in line:
        if char not in charachters:
            charachters.append(char)
print(total)
