from itertools import combinations

N, M = map(int, input().split())

nums = list(map(int, input().split()))

sums = list(combinations(nums, 3))

difference = 300001
for s in sums:
    pin = sum(s)
    if pin <= M and M - pin < difference:
        difference = M - pin
        answer = pin

print(answer)