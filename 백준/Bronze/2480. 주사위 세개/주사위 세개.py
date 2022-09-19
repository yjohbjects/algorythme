a, b, c = map(int, input().split())

score = 0
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
if a == b and b == c:
    score = 10000 + (a * 1000)

# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
elif a == b and b != c:
    score = 1000 + (a * 100)
elif a == c and b != c:
    score = 1000 + (a * 100)
elif b == c and a != b:
    score = 1000 + (b * 100)

# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
elif a != b and b != c and c != a:
    maxV = max(a, b, c)
    score = maxV * 100

print(score)