def solution(my_string, n):
    answer = ''
    
    for letter in my_string:
        answer += letter * n
        
    return answer