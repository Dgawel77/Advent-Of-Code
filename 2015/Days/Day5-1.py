def Vowels():
    has = 0
    vowels = ["a","e","i","o","u"]
    for char in line:
        if char in vowels:
            has += 1
    return True if has >= 3 else False

def Row():
    for i in range(0, len(line)-1):
        if line[i] == line[i+1]:
            return True
    return False

def NotHave():
    has = ["ab", "cd", "pq", "xy"]
    for part in has:
        if part in line:
            return False
    return True

with open("Python\\Advent-Of-Code\\2015\\Input\\Day5Input.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    if Vowels() and Row() and NotHave():
        total += 1
print(total)