while True:
    num = int(input())
    answer = 0

    if num == 0:
        break

    else:
        for i in range(1, num + 1):
            answer += i

    print(answer)