def solution(n):
    answer = 0
    piece = n

    while True:
        if piece % 6 == 0:
            answer = piece // 6
            break
        else:
            piece += n
            continue
            
    return answer