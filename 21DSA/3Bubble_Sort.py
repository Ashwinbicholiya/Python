nums = [8,5,14,42,11,45]

for i in range(len(nums)-1,0,-1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print(nums)

 