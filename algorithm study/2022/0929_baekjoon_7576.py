# 토마토
from collections import deque
def bfs(que):
    while que:
        ti, tj = que.popleft()
        for di, dj in delta:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M and storage[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                day = days[ti][tj] + 1
                if day < days[ni][nj]:
                    days[ni][nj] = day
                    que.append([ni,nj])

from sys import stdin
M, N = map(int, stdin.readline().split())
storage = [list(map(int, stdin.readline().split())) for _ in range(N)]
days = [[1000000]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

cnt = 0
que = deque([])
for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:      # 익은 토마토 = bfs를 시작해야하는 지점
            days[i][j] = 0          # day = 0
            visited[i][j] = 1       # 방문처리한 후
            que.append([i, j])      # 인큐
        elif storage[i][j] == -1:
            days[i][j] = -1
bfs(que)                            # 익은토마토 위치 싹 가지고 bfs들어감
                                    # bfs끝나면 days에 각 위치의 최소day가 적히고
                                    # 그 중 max값이 출력해야 할 답

ans = [0]*N                         # 여기서부터는 출력할려고 한 짓
for i in range(N):
    if max(days[i]) < 1000000:
        ans[i] = max(days[i])
    else:
        ans = 1000000
        break

try:
    print(max(ans))
except TypeError:
    print(-1)