# 아기 상어
from collections import deque
from sys import stdin
# 1. (i,j)에서 (fi,fj)로 가는 최단거리를 반환하는 함수
def min_dstc(i, j, fi, fj, shark):
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    que = deque([[i, j]])
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and area[ni][nj] <= shark:
                visited[ni][nj] = 1
                distance[ni][nj] = distance[si][sj] + 1
                que.append([ni, nj])
                if [ni, nj] == [fi, fj]:
                    return distance[ni][nj]
    return 0

# 2. 현재 위치(i,j)에서 먹으러 가야할 물고기의 위치(fi,fj)를 반환하는 함수.
def can_eat(i, j, shark,):
    for f in range(len(fishes)):
        fi, fj, d, size = fishes[f]
        if size < shark:
            fishes[f][2] = min_dstc(i, j, fi, fj, shark)
    fishes.sort(key=lambda x:(x[2], x[0], x[1]))            # 가장 가깝고, 가장 위이며, 가장 왼쪽

    for fi, fj, d, size in fishes:
         if [fi, fj] not in isEaten and size < shark and d > 0:
            # print('.........................')
            # print(f'다음 물고기 : {fi, fj,}, 상어 크기 : {shark} ')
            return fi, fj, shark

    return 0                                                # 먹을 물고기가 없다면 0 반환


# 3. 시작지점부터 물고기를 먹어가면서 이동한 거리를 cnt에 계속 더해주는 함수.
def bfs(i, j, shark, eat):
    global cnt

    while len(isEaten) != len(fishes):              # 모든 물고기를 먹거나, 먹을 물고기가 없을 때까지 반복.
        try:
            ti, tj, shark = can_eat(i, j, shark)        # 먹으러갈 물고기 위치 반환됨
        except TypeError:                               # 먹을 물고기가 없어 0이 반환되면 TypeError뜨고 종료
            return

        cnt += min_dstc(i, j, ti, tj, shark)            # 최단 거리 cnt에 ++
        isEaten.append([ti, tj])
        eat += 1
        if eat == shark:
            shark += 1
            eat = 0
        i, j = ti, tj
        # print(f'먹은 물고기 : {isEaten}')
        # print(f'상어 크기 : {shark}, 먹은 횟수 : {eat}, 타임 : {cnt}')
        # print('.........................')

N = int(stdin.readline())
area = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
delta = [[-1,0],[0,-1],[1,0],[0,1]]

si = sj = 0
fishes = []             # 맵에 존재하는 모든 물고기가 담기는 리스트
isEaten = []            # 먹은 물고기 담기는 리스트
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            si, sj = i, j
        elif 1 <= area[i][j] <= 6:
            fishes.append([i, j, N**2, area[i][j]])  # i, j, 아기상어와의 거리, 물고기 크기

area[si][sj] = 0     # 시작 자리도 지나다닐 수 있게 0으로 만듦
cnt = 0              # 모든 최단거리의 합
bfs(si, sj, 2, 0)    # 상어 좌표, 상어크기, 먹은 개수
print(cnt)