def solution(my_string):
    answer = 0
    for letter in my_string:
        if letter.isnumeric():
            answer += int(letter)
    return answer