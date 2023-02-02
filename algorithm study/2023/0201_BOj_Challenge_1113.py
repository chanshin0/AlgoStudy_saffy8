'''
반례
4 5
59995
95549
94449
88888
'''
# 수영장 만들기
N, M = map(int, input().split())
area = [list(map(int, input())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]
# print(area)
visited = [[0]*M for _ in range(N)]
# print(visited)

if N < 3 or M < 3:
    print(0)
    exit(0)

wall = []
need_check = []
for i in range(N):
    for j in range(M):
        if 1 <= i < N-1 and 1 <= j < M-1:
            need_check.append((i,j))
        else:
            wall.append((i,j))

# A = (ni,nj)
# 1. A가 나보다 큼  : A가 벽이든 아니든 물을 넣을 수 있음
# 2. A가 작거나 같음 : A가 벽이면 X, A가 벽이 아니면 넣을 수 있음
# 3. 4방향 델타중에 한번이라도 X가 있으면 벽으로 취급함.
from collections import deque
maxV = max(map(max, area))
que = deque(need_check)
water = 0
while que:
    ki, kj = que.popleft()
    available = True
    for di, dj in delta:
        ni,nj = ki+di,kj+dj
        if area[ni][nj] > area[ki][kj]:
            pass
        else:
            if (ni,nj) in wall or area[ki][kj] >= maxV:
                available = False
                break
            else:
                pass
    if available:
        area[ki][kj] += 1
        water += 1
        que.append((ki,kj))
    else:
        wall.append((ki,kj))

print(water)
for i in range(N):
    print(area[i])