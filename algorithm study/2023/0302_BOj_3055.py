# 탈출
from sys import stdin
from collections import deque

def bfs(i, j, Di, Dj, s):
    visited[i][j] = 1
    que = deque([(i,j)])
    if s == "S":
        while que:
            si,sj = que.popleft()

            for di,dj in delta:
                ni,nj = si+di, sj+dj
                if 0 <= ni < R and 0 <= nj < C and area[ni][nj] in ['D','.'] and not visited[ni][nj]:
                    if area[ni][nj] == 'D':
                        return visited[si][sj]
                    visited[ni][nj] = visited[si][sj] + 1
                    que.append((ni,nj))
        return 0

    elif s == "water":
        while que:
            si, sj = que.popleft()

            for di,dj in delta:
                ni,nj = si+di, sj+dj
                if 0 <= ni < R and 0 <= nj < C and area[ni][nj] == '.':
                    if not visited[ni][nj] or visited[ni][nj] > visited[si][sj] + 1:
                        visited[ni][nj] = visited[si][sj] + 1
                        que.append((ni,nj))

        if visited[Di][Dj]:
            return max(map(max, visited)) -1
        else:
            return 0

        # print('...............')
        # print(si, sj)
        # for i in range(R):
        #     print(visited[i])
        # for i in range(R):
        #     print(area[i])
        # print(que)
        # print('...............')

R, C = map(int, input().split())
area = [list(input()) for _ in range(R)]
# print(area)
delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[0] * C for _ in range(R)]

Di = Dj = 0
Si = Sj = 0
waters = []
min_water = 50*50+1
for i in range(R):
    for j in range(C):
        if area[i][j] == 'S':
            Si,Sj = i,j
        elif area[i][j] == '*':
            waters.append((i,j))
        elif area[i][j] == 'D':
            Di,Dj = i,j

ans = bfs(Si,Sj, Di, Dj, "S")
if not ans:
    print("KAKTUS")
    exit(0)

for wi, wj in waters:
    temp = bfs(wi, wj, Di, Dj, "water")
    if temp:
        min_water = min(min_water, temp)

print(ans, min_water)
print(ans) if min_water > ans else print("KAKTUS")


