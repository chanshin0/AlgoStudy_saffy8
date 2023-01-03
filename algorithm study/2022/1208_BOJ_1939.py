# 중량제한
from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())
INF = 1000000000
adjL = [0]*(N+1)
# adjM = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    if adjL[s] < w:
        adjL[s] = w
    if adjL[e] < w:
        adjL[e] = w
# print(adjL)

    # if adjM[s][e] < w:
    #     adjM[s][e] = w
    # if adjM[e][s] < w:
    #     adjM[e][s] = w
# print(adjM)
A, B = map(int, input().split())


print(min(adjL[A], adjL[B]))
