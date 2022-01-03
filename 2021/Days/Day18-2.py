with open('../Input/Day18input.txt') as f:
    lines = f.read().splitlines()


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
        resetactive = False
        while x < len(s):
            if s[x].isnumeric() and s[x+1].isnumeric():
                s = s[:x] + split(s[x]+s[x+1]) + s[x+2:]
                # print('split  ', s)
                resetactive = True
                break
            x += 1
        active = resetactive
    return s


maximum = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            q = reduce('[' + lines[i] + ',' + lines[j] + ']')
            maximum = max(maximum, coolerMagnitude(q))
print(maximum)
