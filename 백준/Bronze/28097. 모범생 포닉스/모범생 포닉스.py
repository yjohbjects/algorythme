N = int(input())
plans = list(map(int, input().split()))

total = sum(plans) + (len(plans) - 1) * 8

print(total // 24, total % 24)