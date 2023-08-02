N = int(input())

for _ in range(N):
    d, f, p = map(float, input().split())
    answer = d * f * p
    print('$%.2f' % answer)