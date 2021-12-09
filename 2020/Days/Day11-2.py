def showanswer():
    for x in enumerate(answer):
        for y in answer[x[0]]:
            print(y, end="")
        print()
    print()

def solve(x, y):
    openSeatsNearby, mult, remove= 0, 0, []
    pathways = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    while pathways != []:
        mult += 1
        for cord in pathways:
            newX = x + cord[0]*mult
            newY = y + cord[1]*mult
            #if ((newX > len(previous)-1) or (newX < 0)) or ((newY > len(previous[0])-1) or (newY < 0)):
            if ((newX > len(previous)-1) or (newX < 0)) or ((newY > len(previous[0])-1) or (newY < 0)):
                remove.append(cord)
            elif previous[newX][newY] == "#":
                openSeatsNearby += 1
                remove.append(cord)
            elif previous[newX][newY] == "L":
                remove.append(cord)
        for out in remove:
            pathways.remove(out)
        remove.clear()
    return openSeatsNearby


with open("Advent2020\Day11Input.txt") as f:
    lines = f.read().split("\n")
previous, answer = [], []
for line in enumerate(lines):
    previous.append([])
    answer.append([])
    for char in line[1]:
        previous[line[0]].append(char)
        answer[line[0]].append(".")

while True:
    for line in enumerate(previous):
        for seat in enumerate(line[1]):
            if seat[1] == "L":
                if solve(line[0], seat[0]) == 0:
                    answer[line[0]][seat[0]] = "#"
            elif seat[1] == "#":
                if solve(line[0], seat[0]) >= 5:
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
