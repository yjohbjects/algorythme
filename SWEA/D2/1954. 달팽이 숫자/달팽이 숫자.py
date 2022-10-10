T = int(input())
for t in range(1, T+1):
    N = int(input())

    snail_nums = [[[] for _ in range(N)] for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우하좌상
    i = 1
    x, y = 0, 0
    direction = 0

    snail_nums[0][0] = i
    while i < N * N:

        # 이동 가능한 곳이라면 이동
        if 0 <= x + dxy[direction][0] < N and 0 <= y + dxy[direction][1] < N and not snail_nums[x + dxy[direction][0]][y + dxy[direction][1]]:
            # 이동
            x += dxy[direction][0]
            y += dxy[direction][1]

            # 값 입력
            i += 1
            snail_nums[x][y] = i

        # 다음 x, y 좌표가 이동 가능하지 않은 좌표라면: 1) 맵 밖,  2) 이미 값이 차있는 좌표
        else:
            # direction을 바꿔준다
            direction = (direction + 1) % 4
            
            # direction을 바꿨는데도 이동할 곳이 없다면? break
            if snail_nums[x + dxy[direction][0]][y + dxy[direction][1]]:
                break

    print(f'#{t}')
    for n in snail_nums:
        print(*n)