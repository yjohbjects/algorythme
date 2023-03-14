def solution(s1, s2):
    answer = 0
    
    for element in s1:
        answer += s2.count(element)
        
    return answer