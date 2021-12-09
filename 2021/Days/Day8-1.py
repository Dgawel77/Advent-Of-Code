with open('Python\\Advent-Of-Code\\2021\\Input\\Day8input.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
    signal, output = line.strip().split(' | ')
    output = output.split()
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            total += 1
print(total)
