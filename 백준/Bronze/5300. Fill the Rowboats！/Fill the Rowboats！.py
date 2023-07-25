N = int(input())
answer = ''
for i in range(1, N):
    if i % 6 == 0:
        answer += str(i) + ' Go! '

    else:
        answer += str(i) + ' '

answer += str(N) + ' Go!'
print(answer)