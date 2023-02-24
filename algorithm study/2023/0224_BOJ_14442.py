# 벽 부수고 이동하기 2
from sys import stdin
from collections import deque
input = stdin.readline
N, M, K = map(int, input().split())
area = [list(map(int, input().strip())) for _ in range(N)]

delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K+1)]
# print(visited)

def bfs(i, j):
    visited[K][i][j] = 1
    que = deque([(i,j,K)])
    while que:
        si, sj, k = que.popleft()
        if (si, sj) == (N-1, M-1):
            return visited[k][si][sj]

        for di,dj in delta:
            ni,nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[k][ni][nj] and not area[ni][nj]:
                visited[k][ni][nj] = visited[k][si][sj] + 1
                que.append((ni, nj, k))

            if k > 0:
                if 0 <= ni < N and 0 <= nj < M and not visited[k-1][ni][nj] and area[ni][nj]:
                    visited[k-1][ni][nj] = visited[k][si][sj] + 1
                    que.append((ni, nj, k-1))
    return -1

print(bfs(0,0))
