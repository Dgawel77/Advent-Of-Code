with open("Day5Input2.txt") as f:
    numbers = list(map(int, f.readlines()))
numbers.sort()
for x in range(0, len(numbers)-1):
    if numbers[x]+1 == numbers[x+1]-1:
        print(numbers[x]+1)
    
