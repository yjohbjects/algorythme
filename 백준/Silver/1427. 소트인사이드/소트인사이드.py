nums = list(input())

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums = sorted(nums, reverse=True)

for i in range(len(nums)):
    nums[i] = str(nums[i])

a = ''.join(nums)
print(a)