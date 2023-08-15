N = int(input())

for _ in range(N):
    num = int(input())
    
    answer = 0
    for i in range(1, num +  1):
        if i % 2 == 1:
            answer += i
        
    print(answer)
