N, M = map(int, input().split())

answer = 0
if N > 0:
    books = list(map(int, input().split()))

    temp = 0

    for book in books:
        if temp + book > M:
            answer += 1
            temp = book
        else:
            temp += book

    if temp > 0:
        answer += 1

print(answer)

