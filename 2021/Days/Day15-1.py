from typing import Deque

with open('Python\\Advent-Of-Code\\2021\\Input\\Day15input.txt') as f:
    lines = list(map(lambda x: [int(c) for c in x], f.read().split("\n")))


class dijkstra:
    def __init__(self, g, height, width):
        self.g = g
        self.spt = dict.fromkeys(g.keys(), float('inf'))
        self.height = height
        self.width = width

    def bfs(self, r, c):
        queue = Deque([(r, c, 0)])
        while len(queue) > 0:
            r, c, cost = queue.popleft()
            next = [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]
            for nr, nc in next:
                if 0 <= nr < self.height and 0 <= nc < self.width:
                    if (cost + self.g[(r, c)] < self.spt[(nr, nc)]):
                        self.spt[(nr, nc)] = cost + self.g[(r, c)]
                        queue.append((nr, nc, cost + self.g[(r, c)]))

    def dijkstra(self, sr, sc, tr, tc):
        self.bfs(sr, sc)
        return self.spt[(tr, tc)] + self.g[(tr, tc)]


g = {}
for r in range(len(lines)):
    for c in range(len(lines[r])):
        g[(r, c)] = lines[r][c]
g[(0, 0)] = 0

d = dijkstra(g, len(lines), len(lines[0]))
print(d.dijkstra(0, 0, len(lines)-1, len(lines[0])-1))
