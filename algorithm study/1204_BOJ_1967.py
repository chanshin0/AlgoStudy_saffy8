# 트리의 지름
def myorder(s, weight):
    global leaf, ismax

    if s != leaf and s in leafs:
        if ismax < weight:
            ismax = weight
        return

    for e, w in nodes[s]:
        if not visited[e] and sum(visited[1:]) != N:
            visited[e] = 1
            myorder(e, weight+w)

from sys import stdin
input = stdin.readline

N = int(input())

nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))


leafs = []
for n in range(1, N+1):
    if len(nodes[n]) == 1:
        leafs.append(n)

ismax = 0
checked = []
for leaf in leafs:
    visited = [0]*(N+1)
    visited[leaf] = 1
    myorder(leaf, 0)

print(ismax)