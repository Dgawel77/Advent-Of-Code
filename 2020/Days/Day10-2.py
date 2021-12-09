with open("Advent2020\Day10Input.txt") as f:
    nums = list(map(int, f.readlines()))
    nums.append(0)
    nums.append(max(nums)+3)
    nums.sort()
chart = list(map(lambda x: 0, range(0, len(nums)-1)))
chart[-1] = 1

for x in reversed(range(0, len(chart)-1)):
    for i in enumerate(nums[x+1:x+4]):
        if (i[1] - nums[x]) in [1,2,3]:
            chart[x] += chart[x+1+i[0]]
print(chart[0])

#def valid(x):
#    if x == len(nums)-1:
#        return 1
#    positions = 0
#    for check in enumerate(nums[x+1:x+4]):
#        if (check[1] - nums[x]) in [1,2,3]:
#            positions += valid(check[0]+x+1)
#    return positions