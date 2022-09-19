A, B = map(int, input().split())
nums = list(map(int, input().split()))

result = []
for num in nums:
    if num < B:
        result.append(num)
print(*result)
