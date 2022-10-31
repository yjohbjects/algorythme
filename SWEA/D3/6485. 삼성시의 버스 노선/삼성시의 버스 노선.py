# S6485 삼성시의 버스노선

T = int(input())
for t in range(1, T+1):
    lines = [0] * 5001
    N = int(input())

    # 정류장별 겹치는 노선 수 카운트
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            lines[i] += 1

    P = int(input())
    answer = [0] * P
    for i in range(P):
        answer[i] = lines[int(input())]

    print(f'#{t}', end=' ')
    print(*answer)

