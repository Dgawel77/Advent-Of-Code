def solve(x, adress):
    if x >= len(mask):
        memory[adress] = value
        return
    if mask[x] == "X":
        adress = (1 << x) | adress
        solve(x+1, adress)
        adress = (adress & ~(1 << x))
        solve(x+1, adress)
    elif mask[x] == "1":
        adress = (1 << x) | adress
        solve(x+1, adress)
    elif mask[x] == "0":
        solve(x+1, adress)
    return

with open("Advent2020\Day14Input.txt") as f:
    lines = f.readlines()
memory = {}
for line in lines:
    split = line.split()
    if split[0] == "mask":
        mask = split[2][::-1]
    else:
        value = int(split[2])
        adress = int(split[0][4:-1])
        solve(0, adress)
print(sum(memory.values()))