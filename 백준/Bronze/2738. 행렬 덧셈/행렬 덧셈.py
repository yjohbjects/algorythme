N, M = map(int, input().split())

list1 = []
list2 = []
for _ in range(N):
    list1.append(list(map(int, input().split())))

for _ in range(N):
    list2.append(list(map(int, input().split())))

answer = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        answer[i][j] = list1[i][j] + list2[i][j]

for a in answer:
    print(*a)