def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[0] * numbers[1] if numbers[0] * numbers[1] >= numbers[-1] * numbers[-2] else numbers[-1] * numbers[-2]
    return answer