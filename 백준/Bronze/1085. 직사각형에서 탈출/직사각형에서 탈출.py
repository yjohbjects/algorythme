x, y, w, h = map(int, input().split(' '))
print(min([abs(x - 0), abs(y-0), abs(x-w), abs(y-h)]))
