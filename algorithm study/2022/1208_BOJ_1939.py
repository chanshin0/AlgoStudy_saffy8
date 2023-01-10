# 중량제한
from sys import stdin
input = stdin.readline
from collections import deque

def dfs(s):


    for i in range(1, N+1):
        if adjM[s][i] and not visited[i]:
            if i == B:
                return True
            visited[i] = 1
            dfs(i)


N, M = map(int, input().split())
INF = 1000000000
# adjL = [0]*(N+1)
adjM = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())

# print(adjL)

    if adjM[s][e] < w:
        adjM[s][e] = w
    if adjM[e][s] < w:
        adjM[e][s] = w
print(adjM)
A, B = map(int, input().split())

visited = [0]*(N+1)
visited[A] = 1
print(dfs(A))
print(visited)

low = 1
high = 1000000000
mid = (low+high)//2 + 1

while mid < high:
    dfs(mid)