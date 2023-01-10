# 전쟁 - 전투
def dfs(i, j, S):
    visited[i][j] = 1
    global cnt
    for di, dj in delta:
        ni = i+di
        nj = j+dj
        if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and battle[ni][nj] == S:
            cnt += 1
            dfs(ni, nj, S)


N, M = map(int, input().split())
battle = [list(input()) for _ in range(M)]

W = 0
B = 0
visited = [[0]*N for _ in range(M)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            cnt = 1
            dfs(i,j,battle[i][j])
            if battle[i][j] == 'W':
                W += cnt**2
            else:
                B += cnt**2

print(W, B)
