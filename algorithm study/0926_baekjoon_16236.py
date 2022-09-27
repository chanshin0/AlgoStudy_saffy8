# 아기 상어
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

si = sj = 0
fishes = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            si, sj = [i, j]
        elif 1 <= area[i][j] <= 6:
            fishes.append([i, j])


distance = []
for i, j in fishes:
    if area[i][j] < 2:                            # 먹을 수 있으면.
        distance.append(abs(si-i)+abs(sj-j))      # 가까운애를 먹으러 간다

# 거리
for i, j in fishes:
    distance.append(abs(si-i)+abs(sj-j))

delta = [[-1,0],[0,-1],[1,0],[0,1]]     # 위 왼 아 오
visited = [[0]*N for _ in range(N)]

cnt = 1
que = [[si, sj]]
while que:
    bi, bj = que.pop(0)
    for di, dj in delta:
        ni, nj = bi+di, bj+dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = visited[bi][bj] + 1
            que.append([ni, nj])
print(visited)