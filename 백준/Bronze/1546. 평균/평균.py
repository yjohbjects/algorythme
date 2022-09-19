N = int(input())
scores = list(map(int, input().split()))

maxV = 0
for score in scores:
    if score > maxV:
        maxV = score

sum = 0
for i, score in enumerate(scores):
    scores[i] = score/maxV * 100
    sum += scores[i]

print(sum/N)
