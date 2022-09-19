receipt = int(input())
N = int(input())

total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a * b

if total == receipt:
    print('Yes')
else:
    print('No')