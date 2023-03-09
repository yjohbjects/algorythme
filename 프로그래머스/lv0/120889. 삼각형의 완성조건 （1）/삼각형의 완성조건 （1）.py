def solution(sides):
    answer = 1
    
    if max(sides) >= sum(sides) - max(sides):
        answer = 2
    
    return answer