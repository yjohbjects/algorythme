def solution(array):
    answer = 0
    
    for item in array:
        for num in str(item):
            if num == '7':
                answer += 1
                
    return answer