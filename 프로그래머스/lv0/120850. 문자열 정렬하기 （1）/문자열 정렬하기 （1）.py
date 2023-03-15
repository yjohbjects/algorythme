def solution(my_string):
    answer = []
    
    for letter in my_string:
        if letter.isnumeric():
            answer.append(int(letter))
            
    answer.sort()
    return answer