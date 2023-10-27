N = int(input())

answer = 0
days = list(map(int, input().split()))

count = 0
for day in days:
    if day > 0:
        count += 1
        answer = max(answer, count)
    elif day == 0:
        answer = max(answer, count)
        count = 0

print(answer)