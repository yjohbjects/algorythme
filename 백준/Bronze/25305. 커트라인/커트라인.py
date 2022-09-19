# B25305 커트라인

N, k = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if scores[j] > scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]
            
print(scores[-k])