# 캐슬 디펜스
from sys import stdin
N, M, D = map(int, stdin.readline().split())
area = [list(map(int, stdin.readline().split())) for _ in range(N)]

enemy_line = []
for i in range(N):
    tmp = 0
    for j in range(M):
        if area[j][i] == 1:
            tmp += 1
    enemy_line.append(tmp)

