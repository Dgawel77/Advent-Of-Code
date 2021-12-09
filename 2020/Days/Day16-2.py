import itertools
#if a number is valid for the given rule
def valid(num, ruleName):
    for rule in rules[ruleName]:
        range1 = rule.split('-')
        if (int(range1[0]) <= num <= int(range1[1])):
            return True
    return False

#open file
with open("Advent2020\Day16-2Input.txt") as f:
    lines = f.readlines()

#setup dictionaty with all the rules
rules = {}
for line in enumerate(lines):
    if line[1] == '\n':
        space = line[0]
        break
    split = line[1].split(":")
    bothRules = split[1][1:-1].split(" or ")
    rules[split[0]] = bothRules

#set up all a list of all the columns
columns = []
myticket = lines[space+2][:-1].split(",")
for position in range(0, len(lines[space+5].split(","))):
    columns.append([])
    columns[position].append(int(myticket[position]))
    for line in lines[space+5:]:
        split = line[:-1].split(",")
        columns[position].append(int(split[position]))

#setup a dictionary of all possible rules a column can apply to
possible = {}
for column in enumerate(columns):
    for rule in rules:
        if all(map(valid, column[1], itertools.repeat(rule))):
            if rule not in possible:
                possible[rule] = []
            possible[rule].append(column[0])

#Go through every rule and figure out which rule applies to what column
known = {}
while len(known) != len(possible):
    for rule in possible:
        if len(possible[rule]) == 1:
            rem = possible[rule][0]
            known[rule] = rem
            possible[rule] = []
            for name in possible:
                if rem in possible[name]:
                    possible[name].remove(rem)

#make a list of the rules we need to find
keys = []
for line in lines[0:6]:
    split = line.split(":")
    keys.append(split[0])

#find the corresponding values on your ticket and multiply them
answer = 1
for key in keys:
    answer *= int(myticket[int(known[key])])
print(answer)