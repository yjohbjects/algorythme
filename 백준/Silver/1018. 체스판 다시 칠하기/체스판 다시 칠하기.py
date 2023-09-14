N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

answer = 65
start = board[0][0]

# 가능한 8x8 보드 돌기
for i in range(N-7):
    for j in range(M-7):
        start = board[i][j]
        fix = 0

        # 8x8 확인
        for x in range(8):
            for y in range(8):
                a = i + x
                b = j + y

                if x % 2 == 0 and y % 2 == 0:
                    if board[a][b] != start:
                        fix += 1
                elif x % 2 != 0 and y % 2 != 0:
                    if board[a][b] != start:
                        fix += 1
                elif x % 2 == 0 and y % 2 != 0:
                    if board[a][b] == start:
                        fix += 1
                elif x % 2 != 0 and y % 2 == 0:
                    if board[a][b] == start:
                        fix += 1

        fix = min((8 * 8 - fix), fix)

        if fix < answer:
            answer = fix

print(answer)