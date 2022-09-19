T = int(input())

for z in range(1, T+1):
    N, K = map(int, input().split())
    cross = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    garo = []
    sero = []
    for i in range(N):
        for j in range(N):
            # 가로맨
            if cross[i][j] == 1:
                garo.append(cross[i][j])

            elif cross[i][j] == 0:
                if len(garo) == K:
                    cnt += 1
                garo = []


            # 세로맨
            if cross[j][i] == 1:
                sero.append(cross[j][i])

            elif cross[j][i] == 0:
                if len(sero) == K:
                    cnt += 1
                sero = []
        
        # 가로 세로 맨
        if len(garo) == K:
            cnt += 1
        garo = []

        if len(sero) == K:
            cnt += 1
        sero = []


    print(f'#{z} {cnt}')