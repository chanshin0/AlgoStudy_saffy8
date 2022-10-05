# 최단 경로
from collections import deque
def dijk(s):
    d[s] = 0

    que = deque([s])
    while que:
        u = que.popleft()
        if adjL[u]:
            for v, w in adjL[u]:
                if d[v] > d[u]+w:
                    d[v] = d[u]+w
                que.append(v)

from sys import stdin
V, E = map(int, stdin.readline().split())
K = int(stdin.readline().strip())
INF = 11
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    adjL[u].append((v, w))

d = [INF]*(V+1)         # 가중치 담기는 배열
dijk(K)

for i in d[1:]:
    print(i) if i != INF else print('INF')