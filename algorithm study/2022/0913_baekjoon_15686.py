# 치킨 배달
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i,j])
        elif arr[i][j] == 1:
            house.append([i,j])

# 살아남은 모든 경우의 수 리스트
chicken_survived = list(combinations(chicken, M))
possible_distance = []

for c in chicken_survived:  # 경우의 수를 하나씩 꺼냄
    temp_ck = 0                 # 치킨거리후보를 이 변수에 담아서 possible_distane에 저장
    for hi, hj in house:        # 집 하나 꺼내서
        ismin = 0               # 치킨집과의 거리 계산후 최소값을 이 변수에 저장
        for ci, cj in c:
            ck_distance = abs(ci-hi)+abs(cj-hj)
            if ismin == 0 or ismin > ck_distance:
                ismin = ck_distance
        temp_ck += ismin        # 각 집의 치킨거리 최소값을 temp에 담고
    possible_distance.append(temp_ck)
    # 다 더해지면 치킨거리 후보에 저장

print(min(possible_distance))


