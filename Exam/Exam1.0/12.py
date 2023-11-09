nums = [0, 1, 0, 3, 12]
for i in range(nums.count(0)):
    nums.remove(0)
    nums += [0]
print(nums)
