# 영역 구하기
import sys
sys.setrecursionlimit(10**5)

def dfs(i ,j):
    global cnt
    visited[i][j] = 1
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < M and 0 <= nj < N and area[ni][nj]==0 and visited[ni][nj] == 0:
            cnt += 1
            dfs(ni, nj)



from sys import stdin
M, N, K = map(int, stdin.readline().split())
area = [[0]*N for _ in range(M)]
square = [list(map(int, stdin.readline().split())) for _ in range(K)]

for s in square:
    for i in range(s[1], s[3]): # 2 3
        for j in range(s[0], s[2]): # 0 1 2 3
            area[i][j] = 1

cnt_lst = []
delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if area[i][j] == 0 and visited[i][j] == 0:
            cnt = 1
            dfs(i, j)
            cnt_lst.append(cnt)
cnt_lst.sort()
print(len(cnt_lst))
print(*cnt_lst)