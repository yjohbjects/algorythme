def solution(n):
    answer = 0
    
    i = 1
    while True:
        answer += 1
        i = i * answer
        if i > n:
            break
    return answer - 1