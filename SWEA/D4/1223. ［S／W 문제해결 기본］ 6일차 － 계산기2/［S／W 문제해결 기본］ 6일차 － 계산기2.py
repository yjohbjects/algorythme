# 연습문제1 계산기

for t in range(1, 11):
    N = int(input())
    calculate = input()
    postfix = ''
    operators = ['(']

    # 후위 표기법으로 바꾸기
    for char in calculate:
        # operators
        if char == '(':
            operators.append(char)

        elif char == '*' or char == '/':
            while True:
                if operators[-1] == '+' or operators[-1] == '-' or operators[-1] == '(':
                    operators.append(char)
                    break
                elif operators[-1] == '*' or operators[-1] == '/':
                    postfix += operators.pop()

        elif char == '+' or char == '-':
            while True:
                if operators[-1] == '+' or operators[-1] == '-' or operators[-1] == '*' or operators[-1] == '/':
                    postfix += operators.pop()
                else:
                    operators.append(char)
                    break

        elif char == ')':
            while True:
                if operators[-1] == '(':
                    operators.pop()
                    break
                else:
                    postfix += operators.pop()

        # number
        else:
            postfix += char

    while len(operators) > 0:
        if operators[-1] == '(':
            operators.pop()
            continue
        else:
            postfix += operators.pop()
        
    # 계산
    calculator = []
    postfix = list(postfix[::-1])

    for i in range(len(postfix)-1, -1, -1):
        if postfix[i] == '+':
            a = calculator.pop()
            b = calculator.pop()
            postfix.pop()
            calculator.append(int(a) + int(b))
        elif postfix[i] == '-':
            a = calculator.pop()
            b = calculator.pop()
            postfix.pop()
            calculator.append(int(a) - int(b))
        elif postfix[i] == '*':
            a = calculator.pop()
            b = calculator.pop()
            postfix.pop()
            calculator.append(int(a) * int(b))
        elif postfix[i] == '/':
            a = calculator.pop()
            b = calculator.pop()
            postfix.pop()
            calculator.append(int(a) / int(b))

        else:
            calculator.append(postfix[i])

    print(f'#{t} {calculator[0]}')


