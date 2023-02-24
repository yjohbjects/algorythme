def solution(s):
    answer = True
    
    stack = []
    
    for parenthasis in s:
        if not stack or stack[-1] == parenthasis:
            stack.append(parenthasis)
            
        elif stack[-1] == '(' and parenthasis == ')':
            stack.pop()
            
        else:
            stack.append(parenthasis)
        
    if not stack or stack == ['(', ')']:
        answer = True
    else:
        answer = False

    return answer