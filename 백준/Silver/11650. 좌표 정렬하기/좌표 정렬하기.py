N = int(input())

answer = []
for _ in range(N):
    x, y = map(int, input().split())
    answer.append([x, y])

answer = sorted(answer, key=lambda x:(x[0], x[1]))

for item in answer:
    print(*item, sep=' ')
