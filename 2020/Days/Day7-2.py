def DFS(bag):
    global graph, mark
    total = 0
    for w in graph[bag]:
        total += w[1] + (w[1] * DFS(w[0]))
    return total
with open("Advent2020\Day7Input.txt") as f:
    lines = f.readlines()
graph = {}
for line in lines:
    line = line.replace("bags", "bag")
    tag = line.split("bag contain")
    connectTo = tag[1][:-2].split(",")
    if tag[0][:-1] not in graph:
        graph[tag[0][:-1]] = set()
    for connector in connectTo:
        if connector[3:-4] not in graph:
            graph[connector[3:-4]] = set()
        graph[tag[0][:-1]].add((connector[3:-4], int(connector[1])))
print(DFS("shiny gold"))
