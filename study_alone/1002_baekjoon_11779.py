# 최소비용 구하기
def dijk(s, N):
    costs[s] = 0

    for _ in range(N-1):
        u = 0
        minV = INF
        for i in range(1, N+1):
            if costs[i] < minV and not visited[i]:   # 아직 최단거리 결정하지 않은 정점 중 최소값인 것 찾기
                u = i
                minV = costs[i]

        visited[u] = 1

        for i in range(1, N+1):
            if adjM[u][i] != INF:
                if costs[i] > costs[u]+adjM[u][i]:      # 최단거리 갱신 됐으면
                    costs[i] = costs[u]+adjM[u][i]
                    route[i] = u

from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
INF = 100000*N+1
adjM = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, stdin.readline().split())
    if adjM[s][e] > w:
        adjM[s][e] = w
for i in range(N+1):
    adjM[i][i] = 0

S, E = map(int, stdin.readline().split())
costs = [INF]*(N+1)
visited = [0]*(N+1)
route = [0]*(N+1)
dijk(S, N)
# print(costs)
# print(route)
# print(costs[E])

ans = [E]
i = E
while route[i] != 0:
    ans.append(route[i])
    i = route[i]
print(costs[E])
print(len(ans))
print(*ans[::-1])
