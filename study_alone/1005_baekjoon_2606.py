# 바이러스
from collections import deque
from sys import stdin
N = int(stdin.readline())
E = int(stdin.readline())
adjL = [[] for _ in range(N+1)]
for _ in range(E):
    u, v = map(int, stdin.readline().split())
    adjL[u] += [v]
    adjL[v] += [u]
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visited = [0]*(N+1)
que = deque([1])
while que:
    s = que.popleft()
    visited[s] = 1
    if adjL[s]:                     # 인접한 정점이 있으면 반복문 시작
        for e in adjL[s]:
            if not visited[e]:      # s와 인접한 e가 아직 방문되지 않은 곳이라면
                que += [e]       # 어팬드

print(sum(visited)-1)