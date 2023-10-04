N = int(input())

for _ in range(N):
    answer = '*'

    word = input()

    for letter in word:
        if letter != answer[-1]:
            answer += letter
    
    print(answer[1:])