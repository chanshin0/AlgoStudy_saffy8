# 촌수계산
from sys import stdin
input = stdin.readline

n = int(input())
s, e = map(int, input().split())
m = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [0]*(n+1)
que = [s]
visited[s] = 1
while que:
    s = que.pop(0)

    if s == e:
        print(visited[e]-1)
        exit(0)

    if nodes[s]:
        for i in nodes[s]:
            if not visited[i]:
                visited[i] = visited[s] + 1
                que.append(i)

print(-1)