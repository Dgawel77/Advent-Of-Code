with open("Day3Input.txt", "r") as f:
    lines = f.read().split()
moves = [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)]
results = 1
for move in moves:
    x = 0
    resultsMultiplied = 0
    for y in range(0, len(lines), move[1]):
        if lines[y][x] == "#":
            resultsMultiplied += 1
        x += move[0]
        if x > 30:
            x -= 31
    results *= resultsMultiplied
print(results)
        
        
