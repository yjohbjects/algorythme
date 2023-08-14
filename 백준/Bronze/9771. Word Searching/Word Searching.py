s = input()
cnt = 0
try :
    while True :
        lst = input().split()
        for i in lst :
            if s in i : cnt += 1
except :
    print(cnt)