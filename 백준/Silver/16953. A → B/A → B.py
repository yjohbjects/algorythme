A, B = map(int, input().split())

answer = -1
count = 0
while A < B:
    if B % 2 == 1:
        if len(str(A)) < len(str(B)) and str(B)[-1] == '1':
            B = int(str(B)[:len(str(B))-1])
            count += 1
        else:
            break

    else:
        B = B // 2
        count += 1
    
if A == B:
    print(count + 1)

else:
    print(answer)