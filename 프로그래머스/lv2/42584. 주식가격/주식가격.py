def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        stack = []
        for j in range(i, len(prices)):
            stack.append(prices[j])
            if not stack or prices[j] >= stack[0]:
                continue
            else:
                break 
        answer.append(len(stack) - 1)
        
    return answer