# 최소비용 구하기
def dijk(s, n):
    d[s] = 0                # 시작정점 가중치 0

    for _ in range(n-1):
        u = 0                                   # 이번에 최단거리 정할 정점인데
        minV = INF                              # d값이 가장 작은 정점으로 택할 것임
        for i in range(1, n+1):
            if d[i] < minV and not visited[i]:  # 최소값 비교 & 아직 최단거리 결정 안된 곳이어야함
                u = i
                minV = d[i]

        visited[u] = 1                          # 다음 반복문 때 또 돌지 않게 방문처리

        for i in range(1, n+1):                 # 위에서 선택 정점 u에 대해서
            if not visited[i] and adjM[u][i] != INF:   # 인접했고 아직 최단거리 안정해졌다면 & 비용이 0일수도 있음
                d[i] = min(d[i], d[u] + adjM[u][i])

from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
INF = 100000*(N)
adjM = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N):
    adjM[i][i] = 0

for _ in range(M):
    s, e, w = map(int, stdin.readline().split())
    if adjM[s][e] > w:                          # 같은 경로가 여러개 주어질 수 있음
        adjM[s][e] = w
S, E = map(int, stdin.readline().split())

d = [INF]*(N+1)         # 가중치 최소값 담을 리스트
visited = [0]*(N+1)     # 최소값 정했는지 여부
dijk(S, N)
# print(adjM)
# print(d)
print(d[E])