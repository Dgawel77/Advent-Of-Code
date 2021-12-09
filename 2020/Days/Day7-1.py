def DFS(bag):
    global graph, mark, total
    mark[bag] = True
    total = 1
    for w in graph[bag]:
        if not mark[w]:
            total += DFS(w)
    return total
with open("Advent2020\Day7Input.txt") as f:
    lines = f.readlines()
graph, mark = {}, {}
for line in lines:
    line = line.replace("bags", "bag")
    tag = line.split("bag contain")
    connectTo = tag[1][:-2].split(",")
    if tag[0][:-1] not in graph:
        graph[tag[0][:-1]] = set()
        mark[tag[0][:-1]] = False
    for connector in connectTo:
        if connector[3:-4] not in graph:
            graph[connector[3:-4]] = set()
            mark[connector[3:-4]] = False
        graph[connector[3:-4]].add(tag[0][:-1])
print(DFS("shiny gold")-1)