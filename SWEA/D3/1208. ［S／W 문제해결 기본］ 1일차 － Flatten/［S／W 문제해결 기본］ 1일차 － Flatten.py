
for x in range(10):
    dump = int(input())
    piles = list(map(int, input().split()))

    for y in range(dump+1):
        max = 0
        min = 101
        highest = 101
        lowest = 101
        
        # min, max 저장
        for i in range(100):
            if piles[i] >= max:
                max = piles[i]
                highest = i
            if piles[i] < min:
                min = piles[i]
                lowest = i

        # 1회 덤프
        piles[highest] -= 1
        piles[lowest] += 1

    print(f'#{x+1} {max - min}')
