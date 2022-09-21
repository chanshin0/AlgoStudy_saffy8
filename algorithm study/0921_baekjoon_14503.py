# 로봇 청소기
def dfs(r, c, d):
    global cnt
    # 1. 현재 위치를 청소한다
    visited[r][c] = 1
    turn = 0
    # 2. 현재 위치를 기준으로 왼쪽방향부터 탐색한다
    for di, dj in (delta[d:]+delta[:d]):
        idx = delta.index([di, dj])
        ni = r+di
        nj = c+dj
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 and visited[ni][nj] == 0:
        # 2-1. 청소하지 않은 공간이 있으면 회전하고 1번부터 진행한다
            dfs(ni, nj, (idx+1)%4)
            return 1
        # 2-2 청소할 공간이 없으면 2번으로 돌아간다. (다음 for문)
        else:ㅌ
            turn += 1

    # 여기서 끊고 좌표랑 d받아서 벽나올때까지 델타돌리기
    if turn == 4:
        ti, tj = delta[(d+1)%4]
        bi = r + ti
        bj = c + tj
        if 0 <= bi < N and 0 <= bj < M:
            if room[bi][bj] == 1:
                if not dfs(bi, bj, d):
                    return 0
            else:
                dfs(bi, bj, d)


import sys
from sys import stdin
sys.setrecursionlimit(10**5)
N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
room = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

delta = [[0,-1],[1,0],[0,1],[-1,0]] # 북 서 남 동
dfs(r, c, d)
# print(cnt)
ans = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == 0:
            if visited[i][j] == 1:
                ans += visited[i][j]
print(ans)
