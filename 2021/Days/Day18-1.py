# This took a long time to solve. I did not understand the instructions with the
# fact that all explodes happend before splits and splits only happen when explodes cant
# other than that it was ok just took a while to solve. This is not a very clean solution
# I did everything using strings and just which is not very efficient. At first I thought of
# using interloced arrays but that would not work. A tree would have been more efficient.

with open('Python\\Advent-Of-Code\\2021\\Input\\Day18input.txt') as f:
    lines = f.read().splitlines()

# a more pythonic way to calculate the magnitude using eval


def coolerMagnitude(s):
    s = s.translate(str.maketrans({'[': '(3*', ']': '*2)', ',': '+'}))
    return eval(s)


def magnitude(s):
    x = 0
    stack = []
    while x < len(s):
        if s[x] == '[':
            stack.append(x)
        elif s[x] == ']':
            p = stack.pop()
            left, right = map(int, s[p+1:x].split(','))
            s = s[:p] + str(3*left + 2*right) + s[x+1:]
            x = -1
        x += 1
    return int(s)


def split(s):
    number = int(s)
    left = number // 2
    right = number - left
    return '[{},{}]'.format(left, right)


def explode(s, p):
    nextBracket = s[p:].find(']')
    left, right = map(int, s[p+1:p+nextBracket].split(','))
    s = s[:p] + '0' + s[p+nextBracket+1:]
    for x in range(p+1, len(s)):
        if s[x].isnumeric():
            if s[x+1].isnumeric():
                insert = str(int(s[x:x+2])+int(right))
                s = s[:x] + insert + s[x+2:]
            else:
                insert = str(int(s[x])+int(right))
                s = s[:x] + insert + s[x+1:]
            break

    for x in range(p-1, 0, -1):
        if s[x].isnumeric():
            if s[x-1].isnumeric():
                insert = str(int(s[x-1:x+1])+int(left))
                s = s[:x-1] + insert + s[x+1:]
            else:
                insert = str(int(s[x])+int(left))
                s = s[:x] + insert + s[x+1:]
            break
    return s


def reduce(s):
    active = True
    while active:
        x = 0
        core = 0
        while x < len(s):
            if s[x] == '[':
                core += 1
                if core > 4:
                    s = explode(s, x)
                    # print('explode', s)
                    x = -1
                    core = 0
            elif s[x] == ']':
                core -= 1
            x += 1
        x = 0
        active = False
        while x < len(s):
            if s[x:x+2].isnumeric():
                s = s[:x] + split(s[x:x+2]) + s[x+2:]
                # print('split  ', s)
                active = True
                break
            x += 1
    return s


prev = lines[0]
for i in range(1, len(lines)):
    prev = reduce('[' + prev + ',' + lines[i] + ']')

print(coolerMagnitude(prev))
