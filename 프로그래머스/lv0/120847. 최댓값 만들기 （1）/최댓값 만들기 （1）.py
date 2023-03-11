import itertools

def solution(numbers):
    answer = 0
    combs = list(itertools.combinations(numbers, 2))
    for pair in combs:
        if answer < pair[0] * pair[1]:
            answer = pair[0] * pair[1]
    return answer