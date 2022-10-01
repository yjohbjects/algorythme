# S1206 view
# 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보

for t in range(1, 11):
    N = int(input()) # 건물의 개수
    buildings = list(map(int, input().split())) # 건물의 높이

    jomang = 0 # 조망권 카운트
    for i in range(2, len(buildings) - 2):
        # 현재 빌딩이 좌2+우2칸 중 가장 높은 건물이라면
        if buildings[i] > buildings[i - 2] and buildings[i] > buildings[i - 1] and buildings[i] > buildings[i + 1] and buildings[i] > buildings[i + 2]:
            # 조망권에 += 현재 빌딩 - 좌2+우2칸 중 가장 높은 건물
            jomang += buildings[i] - max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])

    print(f'#{t} {jomang}')