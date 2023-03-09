def solution(dot):
    answer = 0
    
    if dot[1] > 0:
        if dot[0] > 0:
            answer = 1
        else:
            answer = 2
    else:
        if dot[0] > 0:
            answer = 4
        else:
            answer = 3
            
    return answer