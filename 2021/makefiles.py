day = int(input('Day: '))
header = 'with open(\'Python\\\\Advent-Of-Code\\\\2021\\\\Input\\\\Day{}input.txt\') as f:\n    lines = f.readlines()\n'.format(day)
with open('Days\\Day{}-1.py'.format(day), 'a') as f:
    f.write(header)

with open('Days\\Day{}-2.py'.format(day), 'a') as f:
    f.write(header)

with open('Input\\Day{}input.txt'.format(day), 'a') as f:
    f.write('This file is empty')
