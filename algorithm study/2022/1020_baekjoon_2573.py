# 빙산
def melting():
    for i, j in ice_bergs:
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj] == 0:
                ice_bergs[(i, j)] -= 1
                if ice_bergs[(i, j)] == 0:
                    break

    for i, j in ice_bergs:
        area[i][j] = ice_bergs[(i, j)]


def is_divided(rest_ice_bergs):
    visited = [[0]*M for _ in range(N)]
    cnt = 1

    for i, j in rest_ice_bergs:
        que = deque([(i, j)])
        visited[i][j] = 1
        while que:
            i, j = que.popleft()
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and area[ni][nj] != 0 and not visited[ni][nj]:
                    cnt += 1
                    visited[ni][nj] = 1
                    que.append((ni, nj))
        break

    if cnt == len(rest_ice_bergs):
        return 0
    else:
        return 1

from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

turn = 0
while True:
    ice_bergs = {}
    for i in range(N):
        for j in range(M):
            if area[i][j] != 0:
                ice_bergs[(i, j)] = area[i][j]

    if not ice_bergs:
        print(0)
        break

    if is_divided(ice_bergs):
        print(turn)
        break

    melting()
    turn += 1
