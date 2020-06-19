def sort(nums):
    for i in range(len(nums)-1, 0 ,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums = []
n = int(input('Enter the length of value '))

for e in range(n):
    val = int(input('Enter the values : '))
    nums.append(val)

sort(nums)
print(nums)