a, b = map(str, input().split())

c = int(a[::-1])
d = int(b[::-1])

if c >= d:
    print(c)

else:
    print(d)