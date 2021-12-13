with open('Python\\Advent-Of-Code\\2021\\Input\\Day12input.txt') as f:
    lines = f.readlines()


def isSmallCave(cave):
    return cave.islower() and cave not in ['start', 'end']


def goToNext(node, next):
    global visited
    if node.islower():
        visited.append(node)
    dfs(next)
    if node.islower():
        visited.remove(node)


visited = []
count = 0
secondVisit = False


def dfs(node):
    global g, count, secondVisit

    if node == 'end':
        count += 1
        return

    for next in g[node]:
        if next not in visited:
            goToNext(node, next)
        elif isSmallCave(next) and not secondVisit:
            secondVisit = True
            goToNext(node, next)
            secondVisit = False


g = {}
for line in lines:
    d, e = line.strip().split('-')
    if d not in g:
        g[d] = []
    if e not in g:
        g[e] = []
    g[d].append(e)
    if d != 'start' or e != 'end':
        g[e].append(d)
dfs('start')
print(count)
