def solution(s):
    nums = list(map(int, s.split(' ')))
    answer = str(min(nums))
    answer += ' '
    answer += str(max(nums))
    return answer