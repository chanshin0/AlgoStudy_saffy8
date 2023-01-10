# 알파벳
from sys import stdin
input = stdin.readline

def dfs(i, j, cnt):
    global ismax
    flag = 0
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < R and 0 <= nj < C and visited[area[ni][nj]] == 0:
            flag = 1
            visited[area[ni][nj]] = 1
            dfs(ni, nj, cnt+1)
            visited[area[ni][nj]] = 0

    if not flag:
        if ismax < cnt:
            ismax = cnt

R, C = map(int, input().split())
area = [list(input().strip()) for _ in range(R)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

visited = {}
for i in range(R):
    for j in range(C):
        visited[area[i][j]] = 0

visited[area[0][0]] = 1
ismax = 0
dfs(0, 0, 1)
print(ismax)
