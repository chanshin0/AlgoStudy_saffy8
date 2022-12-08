# 트리의 지름
def myorder(s):
    global leaf, rst

    if s != leaf and e in leafs:
        return

    if nodes[s]:
        for x, y in nodes[s]:
            if not visited[x]:
                visited[x] = 1
                rst += y
                myorder(x)



from sys import stdin
input = stdin.readline

N = int(input())

nodes = []
for _ in range(N+1):
    nodes.append([])

for _ in range(N-1):
    s, e, w = map(int, input().split())
    nodes[s].append((e,w))
    nodes[e].append((s,w))
print(nodes)


leafs = []
for n in range(1,N+1):
    if  len(nodes[n]) == 1:
        leafs.append(n)
# [7, 8, 9, 10, 11, 12]

from itertools import combinations

targets = list(combinations(leafs, 2))
# [(7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (8, 9), (8, 10), (8, 11), (8, 12), (9, 10), (9, 11), (9, 12), (10, 11), (10, 12), (11, 12)]

ismax = 0
# for leaf in leafs:
#     visited = [0]*(N+1)
#     visited[leaf] = 1
#     rst = 0
#     myorder(leaf)
#     if ismax < rst:
#         ismax = rst
# print(ismax)
print(myorder(4))