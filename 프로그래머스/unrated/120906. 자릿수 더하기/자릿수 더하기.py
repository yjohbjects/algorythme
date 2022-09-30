def solution(n):
    nums = str(n)
    answer = 0
    for num in nums:
        answer += int(num)
    return answer