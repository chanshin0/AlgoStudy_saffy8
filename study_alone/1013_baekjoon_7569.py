# 토마토
import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    global matured
    visited[i][j] = 1
    que = deque([(i, j)])
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N*H and 0 <= nj < M and area[ni][nj] == 0:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[si][sj] + 1
                    que.append((ni, nj))
                    matured += 1
                else:
                    if visited[ni][nj] > 1:
                        if visited[ni][nj] > visited[si][sj] + 1:
                            visited[ni][nj] = visited[si][sj] + 1
                            que.append((ni, nj))
            # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # print(f'이번 위치 : {(ni, nj)}')
            # for i in visited:
            #     print(i)

M, N, H = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N*H)]
delta = [[0, 1],[1, 0],[0,-1],[-1,0]]
for i in range(1, H):
    delta += [N*i,0], [-N*i,0]
print(delta)
visited = [[0]*M for _ in range(N*H)]

check = 0
matured = 0
for i in range(N*H):
    for j in range(M):
        if area[i][j] == 1:
            bfs(i, j)
        if area[i][j] == 0:
            check += 1

if not check:
    print(0)
else:
    print(-1) if check != matured else print(max(map(max, visited))-1)

'''
5 5 2
1 -1 1 -1 1
0 0 -1 -1 1
0 -1 -1 1 0
0 -1 0 0 1
0 0 1 -1 1
1 -1 -1 -1 -1
0 -1 0 1 1
0 1 0 0 -1
-1 -1 -1 -1 -1
-1 0 0 1 -1
답 3
'''