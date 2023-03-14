def solution(my_string):
    answer = ''
    
    for letter in my_string:
        if letter.islower() == True:
            answer += letter.upper()
        else:
            answer += letter.lower()
            
    return answer