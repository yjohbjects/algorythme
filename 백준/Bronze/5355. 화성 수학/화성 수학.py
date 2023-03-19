N = int(input())

for _ in range(N):
    mars = list(input().split(' '))

    answer = float(mars[0])
    for i in range(1, len(mars)):
        if mars[i] == '@':
            answer = answer * 3

        elif mars[i] == '%':
            answer += 5

        elif mars[i] == '#':
            answer -= 7

    print(f'{answer:.2f}')