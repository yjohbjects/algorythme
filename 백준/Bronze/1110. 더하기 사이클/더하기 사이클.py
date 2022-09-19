N = int(input()) # 26
n = N

cnt = 0
while True:
    a = ((n // 10) + (n % 10)) % 10
    b = (n % 10) * 10
    n = a + b
    cnt += 1
    if n == N:
        break

print(cnt)

