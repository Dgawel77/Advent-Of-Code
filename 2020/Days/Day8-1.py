with open("Advent2020\Day8Input.txt") as f:
    lines = f.readlines()
accumulator, line, linenumber, done = 0, lines[0], 0, {}
while line+str(linenumber) not in done:
    done[line + str(linenumber)] = True
    if line[:3] == "acc":
        accumulator+=int(line[4:])
    elif line[:3] == "jmp":
        linenumber += int(line[4:])-1
    linenumber += 1
    line = lines[linenumber]
print(accumulator)