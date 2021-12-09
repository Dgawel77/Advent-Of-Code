startList = [2,0,1,7,4,14,18]
last, places = startList[-1], {}
for item in enumerate(startList[:-1]):
    places[item[1]] = item[0]
for x in range(len(startList)-1, (30000000)-1):
    try: 
        age = x - places[last]
        places[last] = x
        last = age
    except:
        places[last] = x
        last = 0
print(last)
