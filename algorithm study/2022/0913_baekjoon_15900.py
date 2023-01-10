# 나무 탈출
def dfs(l):
    visited[l] = 1
    if l == 1:
        return
    cnt[l] += 1
    for i in node[l]:
        if not visited[i]:
            dfs(i)

import sys
sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
node = [[] for _ in range(N+1)]

for n in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
# [[], [8, 4, 3], [3], [1, 2], [1, 7, 6], [6], [4, 5], [4], [1]]

leaf = []
for i in range(2, N+1):
    if len(node[i]) == 1:
        leaf.append(i)

visited = [0] * (N + 1)
cnt = [0] * (N + 1)
for i in leaf:
    dfs(i)

if sum(cnt)%2:
    print('Yes')
else:
    print('NO')
