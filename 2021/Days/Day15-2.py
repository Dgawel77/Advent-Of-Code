# this code is based off of
# https://github.com/ephemient/aoc2021/blob/main/py/aoc2021/day15.py
# I used the dijkstra algorithm to find the shortest path
# my first iteration in day one was not very good and took a long time
# this solution is cleaner and faster

with open('Python\\Advent-Of-Code\\2021\\Input\\Day15input.txt') as f:
    lines = f.readlines()

import heapq
import math


def dijkstra(risks):
    best = [[math.inf] * len(row) for row in risks]
    best[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0))
    while True:
        r, c = heapq.heappop(queue)
        cost = best[r][c]
        if r == len(risks) - 1 and c == len(risks[r]) - 1:
            return cost
        abj = [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]
        for nr, nc in abj:
            if nr not in range(len(risks)) or nc not in range(len(risks[nr])):
                continue
            newcost = cost + risks[nr][nc]
            if best[nr][nc] > newcost:
                best[nr][nc] = newcost
                heapq.heappush(queue, (nr, nc))


risks = []
for dy in range(5):
    for line in lines:
        risks.append([(int(char) - 1 + dx + dy) %
                      9 + 1 for dx in range(5) for char in line.strip()])
print(dijkstra(risks))
