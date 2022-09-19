T = int(input())
for t in range(T):
    scores = input()

    cnt = 0
    total = 0
    for score in scores:
        if score == 'O':
            cnt += 1
            total += cnt

        else: # 'X'
            cnt = 0

    print(total)