# MooTube

def dijk(s, k):
    visited = [0]*(N+1)
    d = [INF]*(N+1)
    d[s] = 0

    for _ in range(N-1):
        u = 0
        minV = INF
        for i in range(1, N+1):
            if d[i] < minV and not visited[i]:
                u = i
                minV = d[i]

        visited[u] = 1

        for j in range(1, N+1):
            if adjM[u][j] != INF and not visited[j]:
                if d[u] != 0:                           # u가 시작 정점이 아니면
                    d[j] = min(d[j], d[u], adjM[u][j])  #
                else:
                    d[j] = min(d[j], adjM[u][j])
                if d[j] < k:
                    break

    cnt = 0
    for i in d[1:]:
        if i >= k and i != INF:
            cnt += 1

    return cnt

from sys import stdin
N, Q = map(int, stdin.readline().split())

INF = 1000000000+1
adjM = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, stdin.readline().split())
    if adjM[p][q] > r:
        adjM[p][q] = r
    if adjM[q][p] > r:
        adjM[q][p] = r


quests = []
for _ in range(Q):
    k, v = map(int, stdin.readline().split())
    print(dijk(v, k))

# v를 시작 정점으로 하는 그래프에서 최소가중치가 k이상인 것은 몇 개인가?

