# 그림
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[0]*m for _ in range(n)]

howmany = 0
pics = []
visited[0][0] = 1
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            howmany += 1
            cnt = 0
            que = [(i, j)]
            visited[i][j] = 1
            while que:
                si, sj = que.pop(0)
                for di, dj in delta:
                    ni, nj = si+di, sj+dj
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] == 1:
                        visited[ni][nj] = 1
                        cnt += 1
                        que.append((ni, nj))
            pics.append(cnt)

print(howmany)
print(max(pics))
