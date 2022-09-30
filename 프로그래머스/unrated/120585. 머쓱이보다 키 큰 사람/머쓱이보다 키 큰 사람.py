def solution(array, height):
    answer = 0
    for ppl in array:
        if ppl > height:
            answer += 1
    return answer