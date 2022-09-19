nums = list(map(int, input().split()))

result = 0
for num in nums:
    result += num*num

print(result%10)