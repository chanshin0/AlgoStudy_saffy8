# 최소비용 구하기
def dfs(s, e, c):
    global ismin
    if c > ismin:
        return

    if s == e:
        if c < ismin:
            ismin = c
        return

    if node[s]:
        for i in range(len(node[s])):
            a = node[s][i]
            if not visited[a]:
                visited[a] = 1
                dfs(a, e, c+fee[s][i])
                visited[a] = 0
    else:
        return

import sys
N = int(sys.stdin.readline().strip())   # 도시개수
M = int(sys.stdin.readline().strip())   # 버스개수

node = [[] for _ in range(M)]
fee = [[] for _ in range(M)]
for m in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    node[a].append(b)
    fee[a].append(c)
start, end = map(int, sys.stdin.readline().split())
# [[], [2, 3, 4, 5], [4], [4, 5], [5], [], [], []]
# [[], [2, 3, 1, 10], [2], [1, 1], [3], [], [], []]

visited = [0]*(N+1)
ismin = 9999999999999999999999
dfs(start, end, 0)
print(ismin)

