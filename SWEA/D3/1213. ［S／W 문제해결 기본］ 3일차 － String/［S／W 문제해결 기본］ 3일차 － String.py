for z in range(10):
    T = int(input())
    test = input()
    word = input()

    i = 0
    j = 0
    cnt = 0
    while i < len(word) and j < len(test):
        if word[i] != test[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == len(test):
            cnt += 1
            j = 0

    print(f'#{T} {cnt}')