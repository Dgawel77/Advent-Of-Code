time = 1002460
lowest = 10000000000000
IDnum = 0
schedule = "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,601,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37".split(",")
for item in schedule:
    if item != "x":
        if (int(item) - (time % int(item))) < lowest:
            lowest = int(item) - (time % int(item))
            IDnum = int(item)
print(lowest * IDnum)