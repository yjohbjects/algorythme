a, b = map(int, input().split())
c = int(input())

if b+c < 60:
    print(a, b+c)
else:
    m = (b + c) % 60
    h = a + (b + c) // 60
    if h >= 24:
        h -= 24
    print(h, m) # 18 0