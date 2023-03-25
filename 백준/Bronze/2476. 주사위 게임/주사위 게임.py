N = int(input())


answer = 0

for _ in range(N):
    nums = list(map(int, input().split(' ')))
    nums.sort()

    if nums[0] == nums[1] and nums[1] == nums[2]:
        score = 10000 + (nums[0] * 1000)

    elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
        score = max(nums) * 100

    else:
        score = 1000 + (nums[1] * 100)

    if score >= answer:
        answer = score

print(answer)