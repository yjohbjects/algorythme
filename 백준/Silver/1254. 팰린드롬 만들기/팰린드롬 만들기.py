S = input()

answer = 0

# 거꾸로 순회
# ::-1 이 동일한지 확인

comp = []
for i in range(len(S) - 1, -1, -1):
    comp.append(S[i])

    # S[i] 추가했을 때 [::-1]과 동일한지 비교
    if comp == comp[::-1]:
        # 맞다면 answer을 len(comp)로 업데이트
        answer = len(comp) + ((len(S) - len(comp)) * 2)
    
print(answer)

 
