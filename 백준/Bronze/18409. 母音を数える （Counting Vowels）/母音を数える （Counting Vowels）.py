N = int(input())
word = input()
answer = 0
answer += word.count('a')
answer += word.count('e')
answer += word.count('i')
answer += word.count('o')
answer += word.count('u')

print(answer)