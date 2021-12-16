from typing import Deque

with open('Python\\Advent-Of-Code\\2021\\Input\\Day15input.txt') as f:
    lines = list(map(lambda x: [int(c) for c in x], f.read().split("\n")))

class dijkstra:
    def __init__(self, g, height, width):
        self.g = g
        self.spt = dict.fromkeys(g.keys(), float('inf'))
        self.spt[(0, 0)] = 0
        self.visited = set()
        self.height = height
        self.width = width
        
    def bfs(self, r, c):
        queue = Deque([(r, c)])
        while len(queue) > 0:
            r, c = queue.popleft()
            self.visited.add((r,c))
            next = [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]
            for nr, nc in next:
                if 0 <= nr < self.height and 0 <= nc < self.width:
                    self.spt[(nr, nc)] = min(self.spt[(nr, nc)], self.spt[(r,c)] + self.g[(nr, nc)])
                    if (nr, nc) not in self.visited:
                        queue.append((nr, nc))

    def dijkstra(self, sr, sc, tr, tc):
        self.bfs(sr, sc)
        return self.spt[(tr, tc)]

g = {}
for r in range(len(lines)):
    for c in range(len(lines[r])):
        g[(r,c)] = lines[r][c]

#for r in range(len(lines)):
#    for c in range(len(lines[r])):
#        for i in range(5):
#            for j in range(5):
#                x = lines[r][c] + i + j
#                g[(r + (i * len(lines)), c + (j * len(lines[0])))] = 1 + x-10 if x >= 10 else x

g[(0, 0)] = 0
#for r in range(len(lines)*5):
#    print()
#    for c in range(len(lines[0])*5):
#       print(g[(r, c)], end="")

#d = dijkstra(g, len(lines)*5, len(lines[0])*5)
#print(d.dijkstra(0, 0, len(lines)*5-1, len(lines[0])*5-1))

d = dijkstra(g, len(lines), len(lines[0]))
print(d.dijkstra(0, 0, len(lines)-1, len(lines[0])-1))
print("done")
