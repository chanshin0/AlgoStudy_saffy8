# 빵집

from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int, input().split())
area = [list(input().rstrip()) for _ in range(R)]
delta = [[-1,1],[0,1],[1,1]]
visited = [[0]*C for _ in range(R)]
start = [0]*R
cnt = 0

for row in range(R):
    que = deque([(row, 0, [])])
    while que:
        i,j,check = que.popleft()

        if start[row] == 1:

            break
        else:
            if j==C-1:
                start[row] = 1
                cnt += 1
                for ti, tj in check:
                    visited[ti][tj] = 1
                break

            for di,dj in delta:
                ni,nj=i+di,j+dj
                if 0<=ni<R and 0<=nj<C and area[ni][nj] != 'x' and not visited[ni][nj]:
                    check.append((ni,nj))
                    que.append((ni,nj,check))

print(cnt)