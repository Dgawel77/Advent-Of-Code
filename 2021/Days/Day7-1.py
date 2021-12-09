with open('Python\\Advent-Of-Code\\2021\\Input\\Day7input.txt') as f:
    lines = list(map(int, f.read().split(',')))

minimum = float('inf')
for x in range(0, max(lines)):
    total = 0
    for p in lines:
        total += abs(p - x)

    if total > minimum:
        break
    else:
        minimum = total
    # print("x:{} total:{}".format(x, total))
print(minimum)
