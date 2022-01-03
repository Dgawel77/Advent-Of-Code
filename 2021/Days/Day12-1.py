with open('../Input/Day12input.txt') as f:
    lines = f.readlines()


visited = set()
count = 0


def dfs(node):
    global g, count
    if node == 'end':
        count += 1
        return

    for next in g[node]:
        if next not in visited:
            if node.islower():
                visited.add(node)
            dfs(next)
            if node.islower():
                visited.remove(node)


g = {}
for line in lines:
    d, e = line.strip().split('-')
    if d not in g:
        g[d] = []
    if e not in g:
        g[e] = []
    g[d].append(e)
    g[e].append(d)

dfs('start')
print(count)
