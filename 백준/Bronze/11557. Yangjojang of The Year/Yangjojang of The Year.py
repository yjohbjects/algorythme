T = int(input())

for _ in range(T):
    N = int(input())
    answer = ['', 0]
    for _ in range(N):
        uni, drinks = input().split(' ')
        if int(drinks) > answer[1]:
            answer = [uni, int(drinks)]
    print(answer[0])