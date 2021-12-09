with open("Advent2020\Day14Input.txt") as f:
    lines = f.readlines()
values = {}
for line in lines:
    split = line.split()
    if split[0] == "mask":
        mask = split[2]
    else:
        num = int(split[2])
        for bit in enumerate(reversed(mask)):
            if bit[1] == "1":
                num = (1 << bit[0]) | num
            elif bit[1] == "0":
                num = (num & ~(1 << bit[0]))
        values[split[0][4:-1]] = int(num)
print(sum(values.values()))