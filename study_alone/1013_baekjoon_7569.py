# 토마토
import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    visited[i][j] = 1
    que = deque([(i, j)])
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N*H and 0 <= nj < M and area[ni][nj] != -1:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[si][sj] + 1
                    area[ni][nj] = 3
                    que.append((ni, nj))
                else:
                    if visited[ni][nj] > 1:
                        if visited[ni][nj] > visited[si][sj] + 1:
                            visited[ni][nj] = visited[si][sj] + 1
                            area[ni][nj] = 3
                            que.append((ni, nj))

        print('`````````````````````````')
        # print('진행 후 상황')
        # for s in area:
        #     print(s)
        print('visited')
        print(f'이번토마토 : {(i, j)}')
        for s in visited:
            print(s)

M, N, H = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N*H)]
delta = [[0, 1],[1, 0],[0,-1],[-1,0],[N,0], [-N,0]]
visited = [[0]*M for _ in range(N*H)]

check = 0
for i in range(N*H):
    for j in range(M):
        if area[i][j] == 1:
            bfs(i, j)
        if area[i][j] == 0:
            check += 1

if not check:
    print(0)
else:
    minV = min(map(min, area))
    print(-1) if minV == 0 else print(max(map(max, visited))-1)

'''
3 3 2
0 0 1
0 -1 0
1 0 0
0 1 0
-1 0 0
0 0 0
답 3
'''