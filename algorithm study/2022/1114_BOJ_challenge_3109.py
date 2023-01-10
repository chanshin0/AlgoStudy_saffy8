# 빵집
def dfs(i,j):
    global cnt, row
    if j==C-1:
        start[row] = 1
        # cnt += 1
        # for ti,tj in temp:
        #     visited[ti][tj] = 1
        return

    for di, dj in delta:
        ni,nj=i+di,j+dj
        if start[row]:
            return
        if 0<=ni<R and 0<=nj<C and area[ni][nj] != 'x' and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni,nj)

from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
area = [list(input().rstrip()) for _ in range(R)]
delta = [[-1,1],[0,1],[1,1]]
visited = [[0]*C for _ in range(R)]
start = [0]*R
cnt = 0

for row in range(R):
    # s = row
    dfs(row, 0)

for _ in range(R):
    cnt += visited[_][C-1]

print(cnt)