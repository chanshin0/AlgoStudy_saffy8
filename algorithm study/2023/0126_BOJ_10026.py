# 적록색약
import sys
sys.setrecursionlimit(10**6)
N = int(input())
area = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(i,j,C):
    visited[i][j] = C+1
    for di,dj in delta:
        ni,nj = i+di,j+dj
        if 0<= ni < N and 0 <= nj < N and visited[ni][nj]==C:
            if area[i][j] == area[ni][nj]:
                dfs(ni,nj,C)

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,0)
            cnt += 1
        if area[i][j] == 'R':
            area[i][j] = 'G'

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]==1:
            dfs(i,j,1)
            cnt2 += 1

print(cnt, cnt2)