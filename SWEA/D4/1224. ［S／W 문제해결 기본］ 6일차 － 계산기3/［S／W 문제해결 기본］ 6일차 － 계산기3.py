for t in range(1, 11):
    N = int(input())
    calculate = input()
    operators = []
    postfix = ''

    # 후위표현식
    for item in calculate:
        # 스택이 비어있을 경우 push
        if len(operators) == 0:
            operators.append(item)

        # 연산자 '*'
        elif item == '*':
            while True:
                if operators[-1] == '+' or operators[-1] == '(':
                    operators.append(item)
                    break
                elif operators[-1] == '*':
                    postfix += operators.pop()

        # 연산자 '+'
        elif item == '+':
            while True:
                if operators[-1] == '*' or operators[-1] == '+':
                    postfix += operators.pop()
                else:
                    operators.append(item)
                    break

        # 피연산자면 결과에 붙이기
        elif item.isnumeric():
            postfix += item

        # 여는 괄호면 스택에 저장
        elif item == '(':
            operators.append(item)

        # 닫는 괄호
        elif item == ')':
            while True:
                if operators[-1] == '(':
                    operators.pop()
                    break
                else:
                    postfix += operators.pop()

    # 후위표현식을 계산
    calculator = []
    postfix = list(postfix[::-1])

    for i in range(len(postfix)-1, -1, -1):
        if postfix[i] == '+':
            a = calculator.pop()
            b = calculator.pop()
            postfix.pop()
            calculator.append(int(a) + int(b))
        elif postfix[i] == '*':
            a = calculator.pop()
            b = calculator.pop()
            postfix.pop()
            calculator.append(int(a) * int(b))

        else:
            calculator.append(postfix[i])

    print(f'#{t} {calculator[0]}')