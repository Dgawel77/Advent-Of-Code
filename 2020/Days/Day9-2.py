with open("Advent2020\Day9Input.txt") as f:
    lines = f.readlines()
for i in range(0, len(lines)):
    total = int(lines[i][:-1])
    if total > 1038347917:
        break
    sequence = [total]
    for j in range(i+1, len(lines)):
        if total == 1038347917:
            print(max(sequence) + min(sequence))
        elif total > 1038347917:
            break
        total += int(lines[j][:-1])
        sequence.append(int(lines[j][:-1]))
