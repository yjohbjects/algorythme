n = int(input())
cnt = 99999

# 완전 탐색
# 5x + 3y = n 인지 아닌지

for i in range(n//5 + 1):
    for j in range(n//3 + 1):
        if (5 * i) + (3 * j) == n:
            temp = i + j

            if temp < cnt:
                cnt = temp

print(cnt if cnt != 99999 else -1)