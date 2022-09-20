# 단지번호 붙이기
def dfs(i, j):
    global cnt
    visited[i][j] = 1
    for di, dj in delta:
        ni = i+di
        nj = j+dj
        if 0 <= ni < N and 0 <= nj < N and aparts[ni][nj] == 1 and visited[ni][nj] == 0:
            cnt += 1
            dfs(ni, nj)

from sys import stdin
N = int(stdin.readline())
aparts = [list(map(int, stdin.readline().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

danjis = []
for i in range(N):
    for j in range(N):
        cnt = 1
        if aparts[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            danjis.append(cnt)

print(len(danjis))
print('\n'.join(map(str, sorted(danjis))))
