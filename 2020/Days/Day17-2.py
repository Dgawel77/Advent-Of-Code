#goes through the node given from the list of active nodes and 
#adds 1 to 26 adjacent nodes
def add(node):
    global adjacent
    for z in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                for w in [-1, 0, 1]:
                    try:
                        adjacent[(node[0]+x, node[1]+y, node[2]+z, node[3]+w)] += 1
                    except:
                        adjacent[(node[0]+x, node[1]+y, node[2]+z, node[3]+w)] = 1
    adjacent[node] -= 1

with open("Advent2020\Day17Input.txt") as f:
    lines = f.readlines()

#sets up the data structure for the inital pattern
active = {}
for line in enumerate(lines):
    for char in enumerate(line[1]):
        if char[1] == "#":
            active[(char[0],line[0], 0, 0)] = True

for _ in range(0, 6):
    #makes a dict of every node (active and unactive) and how 
    #many adjacent active modes there are next to it
    adjacent = {}
    for node in active:
        add(node)

    #runs logic to see if a node should stay active, become active
    #or become inactive
    for node in adjacent:
        try:
            if active[node] and (adjacent[node] not in [2, 3]):
                active.pop(node)
        except:
            if adjacent[node] == 3:
                active[node] = True
print(len(active))


