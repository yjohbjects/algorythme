for z in range(10):

    T = int(input())

    words = [input() for _ in range(100)]

    test = ''
    maxV = 0
    for i in range(100):
        for j in range(100):
            x = 0
            test = ''
            while j + x <= 99:
                test += words[i][j+x]
                if test == test[::-1]:
                    if len(test) > maxV:
                        maxV = len(test)
                x += 1

    for j in range(100):
        for i in range(100):
            y = 0
            test = ''
            while i + y <= 99:
                test += words[i + y][j]
                if test == test[::-1]:
                    if len(test) > maxV:
                        maxV = len(test)
                y += 1

    print(f'#{T} {maxV}')