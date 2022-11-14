# 빵집
def dfs(s,i,j,temp):
    global cnt
    if start[s] == 1:
        return
    else:
        if j==C-1:
            start[s] = 1
            cnt += 1
            for ti,tj in temp:
                visited[ti][tj] = 1
            #
            # print(f'row:{s}')
            # for i in range(R):
            #     print(visited[i])
            return

        for di, dj in delta:
            ni,nj=i+di,j+dj
            if 0<=ni<R and 0<=nj<C and area[ni][nj] != 'x' and not visited[ni][nj]:
                temp.append((ni,nj))
                dfs(s, ni,nj,temp)

from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
area = [list(input().rstrip()) for _ in range(R)]
delta = [[-1,1],[0,1],[1,1]]
visited = [[0]*C for _ in range(R)]
start = [0]*R
cnt = 0

for row in range(R):
    dfs(row, row, 0, [])

print(cnt)