T = int(input())
for z in range(T):
    tc_num, num_of_items= map(str, input().split())
    numbers = list(map(str, input().split()))

    # 문자열을 숫자로 변경
    dict = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(int(num_of_items)):
        numbers[i] = dict.index(numbers[i])

    # 버블소트로 숫자 정렬
    for x in range(len(numbers)-1, 0, -1):
        for y in range(0, x):
            if numbers[y] > numbers[y+1]:
                numbers[y], numbers[y+1] = numbers[y+1], numbers[y]

    # 숫자를 다시 문자열로 변경
    for j in range(int(num_of_items)):
        numbers[j] = dict[numbers[j]]

    print(tc_num)
    print(*numbers)