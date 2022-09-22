# 로봇 청소기
def dfs(r, c, d):
    global ans
    # 1. 현재 위치를 청소한다
    if visited[r][c] == 0:
        visited[r][c] = 1

    # 2. 현재 위치를 기준으로 왼쪽방향부터 탐색한다
    for di, dj in (delta[d::-1]+delta[-1:d:-1]):
        idx = delta.index([di, dj])
        ni = r+(-di)
        nj = c+(-dj)
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 and visited[ni][nj] == 0:
        # 2-1. 청소하지 않은 공간이 있으면 회전하고 1번부터 진행한다
            dfs(ni, nj, (idx-1)%4)
            return
        # 2-2 청소할 공간이 없으면 2번으로 돌아간다. (다음 for문)

    ti, tj = delta[(d-1)%4]
    bi = r + ti
    bj = c + tj
    if 0 <= bi < N and 0 <= bj < M and room[bi][bj] == 0:
        dfs(bi, bj, d)
    else:
        return


import sys
from sys import stdin
sys.setrecursionlimit(10**5)
N, M = map(int, stdin.readline().split())
R, C, D = map(int, stdin.readline().split())
room = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]


delta = [[0,-1],[-1,0],[0,1],[1,0]] # 북 동 남 서
ans = 0
dfs(R, C, D)
for i in range(N):
    ans += sum(visited[i])
print(ans)

