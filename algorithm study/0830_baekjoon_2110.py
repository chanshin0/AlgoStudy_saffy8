# 공유기 설치
N, C = map(int, input().split())
house = []
for i in range(N):
    house.append(int(input()))
house.sort()
distance = [0]*N
for i in range(1, N):
    a = house[i] - house[i-1]
    distance[i] = a
print(house)
print(distance)
