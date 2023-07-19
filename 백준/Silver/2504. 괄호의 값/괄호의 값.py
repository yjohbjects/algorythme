gwals = input()

stack = []
is_valid = True

for gwal in gwals:
    if not stack:
        stack.append(gwal)

    elif gwal == '(' or gwal == '[':
        stack.append(gwal)

    # stack[-1] == 괄호
    elif stack[-1] == '(' or stack[-1] == '[':
        if stack[-1] == '(' and gwal == ')':
            stack.pop()
            stack.append(2)

        elif stack[-1] == '[' and gwal == ']':
            stack.pop()
            stack.append(3)

        else:
            is_valid = False

    # stack[-1] == 숫자
    else:
        if len(stack) >= 2:
            if stack[-2] == '[' and gwal == ']':
                number = stack.pop()
                stack.pop()
                stack.append(number * 3)

            elif stack[-2] == '(' and gwal == ')':
                number = stack.pop()
                stack.pop()
                stack.append(number * 2)

        else:
            is_valid = False

    if len(stack) >= 2 and str(stack[-1]).isnumeric() and str(stack[-2]).isnumeric():
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)

if is_valid == False:
    print(0)
elif stack:
    if str(stack[0]).isnumeric() and len(stack) == 1:
        print(stack[0])
    else:
        print(0)
else:
    print(0)

