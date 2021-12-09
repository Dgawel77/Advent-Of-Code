with open("Advent2020\Day10Input.txt") as f:
    nums = list(map(int, f.readlines()))
    nums.append(0)
    nums.append(max(nums)+3)
    nums.sort()
total = [0, 0, 0]
for x in range(0, len(nums)-1):
    diffrence = nums[x+1] - nums[x]
    if diffrence in [1,2,3]:
        total[diffrence-1] += 1
print(total[0]*total[2])