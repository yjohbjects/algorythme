def solution(array, n):
    answer = 100
    array.sort()
    
    for num in array:
        if abs(num - n) < abs(answer - n):
            answer = num
    return answer