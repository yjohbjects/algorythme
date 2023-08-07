# R은 배열에 있는 수의 순서를 뒤집는 함수이고, 
# D는 첫 번째 수를 버리는 함수

from collections import deque

T = int(input())
for _ in range(T):
    reverse = False
    p = input() # 수행할 함수의 조합
    n = int(input())
    temp = input()

    if len(temp) == 2:
        nums = deque([])
    else:
        nums = deque(list(map(int, temp[1:len(temp)-1].split(','))))
    
    flag = True
    for command in p:
        if command == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True

        elif nums:
            if reverse:
                nums.pop()
            else:
                nums.popleft()

        else:
            print('error')
            flag = False
            break
    
    if flag:
        # check reverse
        if reverse:
            nums.reverse()

        # print(nums)
        print(str(list(nums)).replace(' ',''))