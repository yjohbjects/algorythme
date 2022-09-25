n = int(input())

for i in range(n, 1, -1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))