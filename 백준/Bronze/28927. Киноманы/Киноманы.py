a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

if (a * 3) + (b * 20) + (c * 120) > (d * 3) + (e * 20) + (f * 120):
    print('Max')
elif (a * 3) + (b * 20) + (c * 120) < (d * 3) + (e * 20) + (f * 120):
    print('Mel')
else:
    print('Draw')