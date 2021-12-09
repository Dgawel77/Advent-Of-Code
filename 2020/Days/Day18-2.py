#finds the first pair of parenthesis that make a set aka (1+2) not (1+(1+2))
def findset(line):
    firstParen = -1
    for char in enumerate(line):
        if char[1] == "(":
            firstParen = char[0]
        elif char[1] == ")":
            return(firstParen, char[0])
    return (-1, -1)

#finds the first equation with a + operand and if that
#is not the case it finds the first one with a * operand
def findequation(operand, places, noSpace):
    for position in range(0, len(places)):
        if places[position][1] == operand:
            if position-1 != -1:
                start = places[position-1][0]+1
            else:
                start = 0
            if position+1 < len(places):
                end = places[position+1][0]-1
            else:
                end = len(noSpace)
            return (start, end)
    return (-1, -1)

#evaluates the given equation
def evaluate(equation):
    noSpace = equation.replace(" ", "")
    places = []
    for char in enumerate(noSpace):
        if char[1] in ["+","*"]:
            places.append(char)
    
    start, end = findequation('+', places, noSpace)
    if start == -1 and end == -1:
        start, end = findequation('*', places, noSpace)
    
    if len(places) == 1:
        return eval(noSpace)
    else:
        evaluation = str(eval(noSpace[start:end+1]))
        return evaluate(noSpace[:start]+evaluation+noSpace[end+1:])

with open("Advent2020\Day18Input.txt") as f:
    lines = f.readlines()

#runs function
#finds every set and solves it, running it down to one calculation
#after that one calculation it calculates it and adds to sum 
total = 0
for line in lines:
    changing = line
    while True:
        FirstParen, NextParen = findset(changing)
        if NextParen != -1:
            replacment = evaluate(changing[FirstParen+1:NextParen])
            changing = changing[:FirstParen] + str(replacment) + changing[NextParen+1:]
        else:
            total += int(evaluate(changing))
            break
print(total)