# MooTube
def bfs(k, s):
    USADO = [INF]*(N+1)
    USADO[s] = 0

    cnt = 0
    for i in range(1, N+1):
        if i != s:                        # 자기 자신을 제외한 모든 정점 i에 대해서
            if adjM[s][i] != -1:      # s와 i가 인접했다면
                USADO[i] = adjM[s][i]
            else:                         # s와 i가 인접하지 않았다면
                 for j in range(1, N+1):
                    if adjM[i][j] != -1 and adjM[s][j] != -1:   # 어떤 정점 j가 s와도 인접하고 i와도 인접한
                        USADO[i] = min(USADO[j], adjM[i][j])

            if USADO[i] >= k:
                cnt += 1
    # print(USADO)
    return cnt

from sys import stdin
from collections import deque
N, Q = map(int, stdin.readline().split())
INF = 1000000000 + 1
adjM = [[-1]*(N+1) for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, stdin.readline().split())
    if adjM[p][q] == -1 or adjM[p][q] > r:
        adjM[p][q] = r
    if adjM[q][p] == -1 or adjM[q][p] > r:
        adjM[q][p] = r

# for i in range(N+1):
#     adjM[i][i] = 0

for _ in range(Q):
    k, v = map(int, stdin.readline().split())
    print(bfs(k, v))