T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    Y = N % H
    X = N // H + 1

    if N % H == 0:
        Y = H
        X = N // H

    print(X + (Y * 100))