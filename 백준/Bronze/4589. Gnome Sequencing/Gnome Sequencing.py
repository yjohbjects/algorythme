N = int(input())
print('Gnomes:')
for _ in range(N):
    nums = list(map(int, input().split()))
    asc = sorted(nums)
    des = sorted(nums, reverse=True)

    if nums == asc or nums == des:
        print('Ordered')

    else:
        print('Unordered')