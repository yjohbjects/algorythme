T = int(input())
for t in range(T):
    yonsei = 0
    korea = 0

    for _ in range(9):
        Y, K = map(int, input().split())

        yonsei += Y
        korea += K

    if yonsei > korea:
        print('Yonsei')

    elif yonsei < korea:
        print('Korea')

    elif yonsei == korea:
        print('Draw')
