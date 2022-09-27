# B1302 베스트셀러

N = int(input())
shelf = []

for i in range(N):
    book = input()
    is_existed = False
    for i in range(len(shelf)):
        if shelf[i][0] == book:
            shelf[i][1] += 1
            is_existed = True
    if is_existed == False:
        shelf.append([book, 1])

shelf = sorted(shelf, key=lambda x:x[0])
shelf = sorted(shelf, reverse=True, key=lambda x:x[1])

print(shelf[0][0])

