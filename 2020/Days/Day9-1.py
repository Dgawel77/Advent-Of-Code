with open("Advent2020\Day9Input.txt") as f:
    nums = list(map(int, f.readlines()))
for i in range(5, len(nums)):
    Made = False
    for preamble in nums[i-5: i]:
        if nums[i] - preamble in nums[i-5: i]:
            Made = True
            break
    if not Made:
        print(nums[i])
        break