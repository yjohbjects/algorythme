
for z in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV = [0] * 4 # [row, col, dig, dig]

    for i in range(100):
        row_sum = 0
        for j in range(100):
            # print(i, j)
            row_sum += arr[i][j]
            # print(row_sum)
            if row_sum > maxV[0]:
                maxV[0] = row_sum

    for x in range(100):
        col_sum = 0
        for y in range(100):
            col_sum += arr[y][x]
            if col_sum > maxV[1]:
                maxV[1] = col_sum

    dig1_sum = 0
    dig2_sum = 0
    for a in range(100):
        dig1_sum += arr[a][a]
        if dig1_sum > maxV[2]:
            maxV[2] = dig1_sum

        dig2_sum += arr[99-a][a]
        if dig2_sum > maxV[3]:
            maxV[3] = dig2_sum

    result = 0
    for b in range(len(maxV)):
        if maxV[b] > result:
            result = maxV[b]

    print(f'#{T} {result}')
