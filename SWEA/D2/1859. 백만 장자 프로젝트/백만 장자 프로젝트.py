T = int(input())
for t in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    answer = 0 # 최대 이익
    local_max = 0
    for i in range(N-1, -1, -1):
        if price[i] > local_max:
            local_max = price[i]

        if local_max - price[i] > 0:
            answer += local_max - price[i]

    print(f'#{t} {answer}')