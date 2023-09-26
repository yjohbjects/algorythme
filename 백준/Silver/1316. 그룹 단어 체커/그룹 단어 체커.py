N = int(input())

answer = 0
for _ in range(N):
    word = input()

    checker = []
    for letter in word:
        if letter not in checker:
            checker.append(letter)

        elif letter != checker[-1]:
            answer += 1
            break

print(N - answer)
