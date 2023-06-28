answer = 0
N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    if coin > K:
        continue

    else:
        answer += K // coin
        K -= coin * (K // coin)

print(answer)