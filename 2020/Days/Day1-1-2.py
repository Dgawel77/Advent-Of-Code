numbers = []
k = 0
while True:
    try:
        m = int(input())
    except:
        break
    numbers.append(m)
    k += 1
print(numbers)
list1 = list(map(lambda x: x+3, numbers))
print(list1)
