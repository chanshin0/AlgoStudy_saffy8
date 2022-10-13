# 스타트링크
# bfs 연습

from sys import stdin
input = stdin.readline()
from collections import deque

def bfs(s):
    que = deque([s])
    visited[s] = 1
    while que:
        u = que.popleft()
        if u == G:
            return
        if u+U <= F and not visited[u+U]:
            visited[u+U] = visited[u] + 1
            que.append(u+U)
        if u-D > 0 and not visited[u-D]:
            visited[u-D] = visited[u] + 1
            que.append(u-D)


F, S, G, U, D = map(int, input.split())
# 1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000
visited = [0]*(F+1)

bfs(S)
if visited[G]:
    print(visited[G] - 1)
else:
    print('use the stairs')