def showanswer():
    for x in enumerate(answer):
        for y in answer[x[0]]:
            print(y, end = "")
        print()
    print()

def solve(x, y):
    openSeatsNearby = 0
    for xChange in range(-1, 2):
        for yChange in range(-1, 2):
            newX = x + xChange
            newY = y + yChange
            if ((newX > len(previous)-1) or (newX < 0)):
                pass
            elif ((newY > len(previous[0])-1) or (newY < 0)):
                pass
            elif previous[newX][newY] == "#":
                openSeatsNearby += 1
    return openSeatsNearby

with open("Advent2020\Day11Input.txt") as f:
    prev = f.read().split("\n")
previous = []
for p in enumerate(prev):
    previous.append([])
    for char in p[1]:
        previous[p[0]].append(char)

answer = []
for x in range(0, len(previous)):
    answer.append([])
    for _ in range(0, len(previous[1])):
        answer[x].append(".")

while(True):
    for line in enumerate(previous):
        for seat in enumerate(line[1]):
            if seat[1] == "L":
                if solve(line[0], seat[0]) == 0:
                    answer[line[0]][seat[0]] = "#"
            elif seat[1] == "#":
                if solve(line[0], seat[0])-1 >= 4:
                    answer[line[0]][seat[0]] = "L"

    if previous == answer:
        total = 0
        for line in answer:
            for seat in line:
                if seat == "#":
                    total += 1
        print(total)
        break

    for line in enumerate(answer):
        for seat in enumerate(line[1]):
            previous[line[0]][seat[0]] = seat[1]