# B2522 별 찍기 - 12
N = int(input())

for i in range(N-1):
    print(' ' * (N-i-1), end='')
    print('*' * (i+1))

for i in range(N-1, -1, -1):
    print(' ' * (N-i-1), end='')
    print('*' * (i+1))
