# MooTube
def bfs(k, s):
    visited = [0]*(N+1)
    visited[s] = 1
    USADO = [INF] * (N + 1)
    USADO[s] = 0
    check = 0
    not_connected = list(range(1, N+1))
    for v, w in adjL[s]:
        USADO[v] = min(USADO[v], w)
        visited[v] = 1
        check += 1
        not_connected.remove(v)
    not_connected.remove(s)

    while check != N-1:
        for i in not_connected:
            for v, w in adjL[i]:
                if visited[v]:
                    USADO[i] = min(USADO[v], w)
                    visited[i] = 1
                    not_connected.remove(i)
                    check += 1

    cnt = 0
    for i in USADO[1:]:
        if i >= k:
            cnt += 1
    # print(USADO)
    return cnt


from sys import stdin
from collections import deque

N, Q = map(int, stdin.readline().split())
INF = 1000000000 + 1

adjL = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, stdin.readline().split())
    adjL[p].append((q, r))
    adjL[q].append((p, r))
# [[], [(2, 3)], [(1, 3), (3, 2), (4, 4)], [(2, 2)], [(2, 4)]]
# print(adjL)
for _ in range(Q):
    k, v = map(int, stdin.readline().split())
    print(bfs(k, v))

'''
5 3
1 2 3
2 3 2
2 4 4
5 4 1
1 2
4 1
2 5

'''