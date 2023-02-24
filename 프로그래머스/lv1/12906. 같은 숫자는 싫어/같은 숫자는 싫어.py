def solution(arr):
    stack = []
    
    for num in arr:
        if stack:
            if num != stack[-1]:
                stack.append(num)
        else:
            stack.append(num)
    return stack