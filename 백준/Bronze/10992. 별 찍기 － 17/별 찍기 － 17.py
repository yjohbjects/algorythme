# 별 찍기 - 17
# https://www.acmicpc.net/problem/10992

N = int(input())

for i in range(1, N + 1):
    if i == N:
        print(' ' * (N - i) + '*' * (2 * i -1) + ' ' * (N - i))
    elif i == 1:
        print(' ' * (N - i) + '* ')
    else:
        print(' ' * (N - i) + '*' + ' ' * (2 * i -3) + '* ')

