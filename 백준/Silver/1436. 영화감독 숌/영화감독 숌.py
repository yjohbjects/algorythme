vol = int(input())
answer = 0

# 카운트가 vol 될 때 까지
count = 0 
while True:
    # '666'이 있으면 카운트
    if '666' in str(answer):
        count += 1

    # '666'이 없으면 패스
    else:
        pass

    if count == vol:
        break
    
    answer += 1

print(answer)