def solution(my_string):
    answer = ''
    for letter in my_string:
        if letter in 'bcdfghjklmnpqrstvwxyz ':
            answer += letter
    return answer