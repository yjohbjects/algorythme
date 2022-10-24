T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    area = [[] for _ in range(N)]
    for i in range(N):
        area[i] = list(map(int, input().split()))


    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0

            for x in range(M):
                for y in range(M):
                    temp += area[i+x][j+y]
            if temp > maxV:
                maxV = temp
            # print(temp)

    print(f'#{t} {maxV}')