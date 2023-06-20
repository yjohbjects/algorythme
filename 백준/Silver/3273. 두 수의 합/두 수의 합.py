import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

answer = 0
nums.sort()
left, right = 0, N-1

while left < right:
    current = nums[left] + nums[right]

    if current == x:
        answer += 1
        left += 1
        right -= 1

    elif current < x:
        left += 1

    elif current > x:
        right -= 1

print(answer)