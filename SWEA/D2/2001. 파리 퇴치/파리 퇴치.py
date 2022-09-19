T = int(input())

for z in range(1, T+1):
    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]
    paris_num = 0 # 구역별 파리의 합을 임시 저장
    maxV = 0 # 구역별 파리의 합의 최대값 저장
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 구역별 파리의 합 구하기
            # paris_num을 [i][j] 초기화
            paris_num = 0
            for x in range(M):
                for y in range(M):
                    paris_num += paris[i+x][j+y]

            if paris_num > maxV:
                maxV = paris_num

    print(f'#{z} {maxV}')