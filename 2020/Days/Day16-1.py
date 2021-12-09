def valid(num):
    for name in rules:
        for rule in rules[name]:
            range1 = rule.split('-')
            if (int(range1[0]) <= num <= int(range1[1])):
                return True
    return False

with open("Advent2020\Day16Input.txt") as f:
    lines = f.readlines()
rules = {}
for line in enumerate(lines):
    if line[1] == '\n':
        space = line[0]
        break
    split = line[1].split(":")
    bothRules = split[1][1:-1].split(" or ")
    rules[split[0]] = bothRules

error = 0
for line in lines[space+5:]:
    nums = line[:-1].split(",")
    for num in nums:
        if not valid(int(num)):
            error += int(num)
print(error)