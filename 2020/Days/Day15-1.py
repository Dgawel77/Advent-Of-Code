list = [2,0,1,7,4,14,18]
for x in range(len(list), 20):
    found = False
    for item in enumerate(reversed(list[:-1])):
        if list[-1] == item[1]:
            list.append(item[0]+1)
            found = True
            break
    if not found:
        list.append(0)
print(list)