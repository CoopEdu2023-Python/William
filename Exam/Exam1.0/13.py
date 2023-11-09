nums = [0, 1, 0, 3, 2]
for i in range(len(nums)):
    if nums[i] != 0 and i != 0:
        while nums[i-1] == 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
print(nums)
