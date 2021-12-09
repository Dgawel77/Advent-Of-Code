with open("Python\\Advent-Of-Code\\2015\\Input\\Day3Input.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    s = list(map(int, line.split("x")))
    total += s[0]*s[1]*s[2]
    s.remove(max(s))
    total += 2*(s[0] + s[1])
print(total)