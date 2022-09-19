T = int(input())
for z in range(T):
    N = int(input())

    # pascal's triangle 만들어놓기
    pascal = []
    for x in range(1, 11):
        pascal.append([0] * x)

    for i in range(10):
        for j in range(i+1):
            if j == 0 or i == j:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    # 결과 프린트
    print(f'#{z+1}')
    for y in range(N):
        print(*pascal[y])

