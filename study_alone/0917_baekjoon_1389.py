# 케빈 베이컨의 6단계 법칙
def bfs(n):
    bacon[n] += 1
    queue = [n]
    while queue:
        fr = queue.pop(0)
        for i in friend[fr]:
            if bacon[i] == -1:
                queue.append(i)
                bacon[i] = bacon[fr] + 1

from sys import stdin
N, M = map(int, stdin.readline().split())
friend = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)
# [[], [3, 4], [3], [1, 4, 2], [1, 5, 3], [4]]

ismin = [0]*(N+1)
for i in range(1, N+1):
    bacon = [-1]*(N+1)
    bfs(i)
    ismin[i] = sum(bacon[1:])

for i in range(1, N+1):
    if ismin[i] == min(ismin[1:]):
        print(i)
        break