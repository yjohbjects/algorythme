for t in range(10):
    T = int(input())
    board = [[] for _ in range(100)]
    for i in range(100):
        board[i] = list(map(int, input().split()))


    maxV = 0
    diag1 = 0
    diag2 = 0
    for i in range(100):
        # 각 대각선의 합
        diag1 += board[i][i] # 좌상에서 우하
        diag2 += board[99-i][i] # 우상에서 좌하

        # 각 행/열의 합
        row = 0
        column = 0
        for j in range(100):
            row += board[i][j]
            column += board[j][i]
        if row > maxV:
            maxV = row
        if column > maxV:
            maxV = column

    if diag1 > maxV:
        maxV = diag1
    if diag2 > maxV:
        maxV = diag2

    print(f'#{T} {maxV}')