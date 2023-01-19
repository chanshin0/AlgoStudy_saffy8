# 레이저 통신
from collections import deque

def bfs(i, j):
    print(visited[i][j])


    que = deque([(i,j,0)])
    while que:
        si,sj, dir = que.popleft()

        if (si,sj)!=(i,j) and area[si][sj] == 'C':
            return visited[si][sj][1]

        for k in range(4):
            di,dj = delta[k]
            ni,nj = si+di,sj+dj
            if 0<=ni<H and 0<=nj<W and area[ni][nj] != '*':
            # 진입조건.
                if not visited[ni][nj][0] and visited[ni][nj][1] > visited[si][sj][1]:
                    visited[ni][nj][0] = 1
                    if dir != k:
                        visited[ni][nj][1] += 1
                    que.append((ni,nj,k))




W, H = map(int, input().split())
area = [list(input()) for _ in range(H)]
# print(area)
delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[[0,0]]*W for _ in range(H)]
# print(visited[0][0])

for i in range(H):
    for j in range(W):
        if area[i][j] == 'C':
            visited[i][j][0] = 1
            visited[i][j][1] = 0
            ans = bfs(i,j)
            print(ans)
            exit(0)