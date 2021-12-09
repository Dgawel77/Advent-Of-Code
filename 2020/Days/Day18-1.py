#finds the first pair of parenthesis that make a set aka (1+2) not (1+(1+2))
def findset(line):
    firstParen = -1
    for char in enumerate(line):
        if char[1] == "(":
            firstParen = char[0]
        elif char[1] == ")":
            return(firstParen, char[0])
    return (-1, -1)

#finds the position of the next operand starting from startingFrom
def findnextequation(line, startingFrom):
    for char in enumerate(line):
        if char[1] in ["+","*"]:
            return char[0] + startingFrom
    return -1

#evaluates the given equation
def evaluate(equation):
    noSpace = equation.replace(" ", "")
    firstOperand = findnextequation(noSpace, 0)
    secondOperand = findnextequation(noSpace[firstOperand+1:], firstOperand+1)
    if secondOperand == -1:
        return eval(noSpace)
    else:
        evaluation = str(eval(noSpace[:secondOperand]))
        return evaluate(evaluation+noSpace[secondOperand:])

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