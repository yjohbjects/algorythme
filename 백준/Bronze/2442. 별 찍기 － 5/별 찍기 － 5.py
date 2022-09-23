# B2442 별 찍기 - 5
N = int(input())

for i in range(N):
    print(' ' * (N-i-1), end='')
    print('*' * ((2 * i) + 1))