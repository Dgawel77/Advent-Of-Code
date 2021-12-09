def solve():
    accumulator, line, linenumber, done = 0, lines[0], 0, {}
    while line+str(linenumber) not in done:
        done[line + str(linenumber)] = True
        if line[:3] == "acc":
            accumulator+=int(line[4:]) 
        elif line[:3] == "jmp":
            linenumber += int(line[4:])-1    
        linenumber += 1
        if(linenumber >= len(lines)):
            print(accumulator)
            return True
        line = lines[linenumber]
    return False

with open("Advent2020\Day8Input.txt") as f:
    lines = f.readlines()

for x in range(0, len(lines)):
    if lines[x][:3] == "nop":
        lines[x] = lines[x].replace("nop", "jmp")
        if solve():
            print(x+1)
        lines[x] = lines[x].replace("jmp", "nop")
    elif lines[x][:3] == "jmp":
        lines[x] = lines[x].replace("jmp", "nop")
        if solve():
            print(x+1)
        lines[x] = lines[x].replace("nop", "jmp")