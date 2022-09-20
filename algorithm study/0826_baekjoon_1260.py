# DFS와 BFS
def dfs(v):
    visited[v] = 1
    ans.append(v)
    for i in sorted(node[v]):
        if not visited[i]:
            dfs(i)

N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

# [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]
ans = []
stack = [V]
visited = [0]*(N+1)
dfs(V)
print(*ans)

#
# while stack:
#     if stack[-1] not in dfs:
#         top = stack.pop()
#         stack += sorted(node[top], reverse=True)
#         dfs.append(top)
#     else:
#         stack.pop()
#
bfs = []
que = [V]
while que:
    if que[0] not in bfs:
        front = que.pop(0)
        que += sorted(node[front])
        bfs.append(front)
    else:
        que.pop(0)
# print(*dfs)
print(*bfs)





