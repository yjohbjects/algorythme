# B4949 균형잡힌 세상
while True:
    words = input()
    if words == '.':
        break
    stack = []
    answer = 'yes'
    for letter in words:
        if letter == '(' or letter == '[':
            stack.append(letter)

        elif letter == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break

        elif letter == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
            pass

        else:
            pass

    if stack:
        answer = 'no'

    print(answer)