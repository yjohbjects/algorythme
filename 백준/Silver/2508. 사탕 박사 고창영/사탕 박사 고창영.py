def isOnBoard(x, y, N, M):
    if 0 <= x <= N-1 and 0 <= y <= M-1:
        return True
    else:
        return False


TC = int(input())
for _ in range(TC):
    a = input()
    N, M = map(int, input().split())

    box = []
    answer = 0

    for _ in range(N):
        box.append(input())

    for x in range(N):
        for y in range(M):

            if box[x][y] == 'o':
                # 좌우점검
                if isOnBoard(x, y-1, N, M) and isOnBoard(x, y+1, N, M):
                    if box[x][y-1] == '>' and box[x][y+1] == '<':
                        answer += 1

                # 상하점검
                if isOnBoard(x-1, y, N, M) and isOnBoard(x+1, y, N, M):
                    if box[x-1][y] == 'v' and box[x+1][y] == '^':
                        answer += 1
    
    print(answer)