def solution(s):
    s = s.lower()
    s = s.title()

    answer = ''
    is_after_number = False
    for idx, char in enumerate(s):
        if char in '0123456789':
            is_after_number = True
            answer += char

        if is_after_number == True and char not in '0123456789':
            answer += char.lower()
            is_after_number = False

        elif is_after_number == False:
            answer += char
    return answer