def solution(num, k):
    answer = -1
    
    for i in range(len(str(num))):
        if str(num)[i] == str(k):
            answer = i + 1
            break
            
    return answer