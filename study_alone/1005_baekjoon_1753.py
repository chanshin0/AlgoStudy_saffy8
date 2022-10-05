# 최단 경로
def dijk(s):
    d[s] = 0

    for _ in range(V-1):                        # 남은 V-1개의 정점의 최단경로 결정한다
        u = 0                                       # 이번에 최단경로 정할 정점
        minV = INF*V                                # 그 정점의 가중치 값(최단경로)
        for i in range(1, V+1):                     # 1~V 정점에 대하여
            if not visited[i] and d[i] < minV:      # 아직 결정되지 않았고, 가중치가 모든 정점 중 최소값이라면
                u = i                               # 이번에 선택하겠다
                minV = d[i]

        visited[u] = 1                              # 다음 반복문 때 또 선택되지 않게 표시

        for j in range(1, V+1):                         # 위에서 선택한 정점 u에 대해서
            if not visited[j] and adjM[u][j] != INF:    # 아직 최단경로 결정되지 않았고, u와 인접해있다면
                d[j] = min(d[j], d[u]+adjM[u][j])       # 최단경로 계산

from sys import stdin
V, E = map(int, stdin.readline().split())
K = int(stdin.readline().strip())
INF = 11
adjM = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    if adjM[u][v] > w:  # 경로가 여러개 주어질 수도 있기 때문에 최소값 비교를 한다.
        adjM[u][v] = w
for i in range(V+1):
    adjM[i][i] = 0

visited = [0]*(V+1)     # 최단경로 결정했는지 여부체크하는 배열
d = [INF]*(V+1)         # 가중치 담기는 배열
dijk(K)

for i in d[1:]:
    print(i) if i != INF else print('INF')