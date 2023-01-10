# 최소 스패닝 트리
def prim(n, v):
    mst = [0]*(V+1)
    mst[n] = 1         # 시작 정점 표시
    w = 0              # mst가중치의 합

    for _ in range(V-1):  # 시작 정점빼고 남은 V-1개의 정점을 정하겠다
        u = 0
        minV = 1000001
        for i in range(1, V+1):             # 정점 i 중에서~
            if mst[i] == 1:                 # mst에 속한 정점이라면,
                for j in range(1, V+1):     # 인접한 정점 j를 탐색한다.
                    # 조건)1.mst에 아직 속하지 않음 and 2.가중치가 존재(인접함을 의미) and 3.가중치가 최소값보다 작으면 선택
                    if mst[j] == 0 and adjM[i][j] > 0 and adjM[i][j] < minV:
                        u = j
                        minV = adjM[i][j]
        # j 탐색이 끝났으면 u와 minV에 최소가중치 조건을 만족하는 정점과 최소가중치가 담긴다
        w += minV       # i와 u 연결하는 최소가중치 더해주고
        mst[u] = 1      # u가 mst에 속했다는것 표시

    return w            # for문 다 돌았으면 w리턴

from sys import stdin
V, E = map(int, stdin.readline().split())
adjM = [([0]*(V+1)) for _ in range(V+1)]        # 1 <= V <= 10000
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    adjM[u][v] = w
    # adjM[v][u] = w
# [[0, 0, 0, 0], [0, 0, 1, 3], [0, 1, 0, 2], [0, 3, 2, 0]]

print(prim(1, V))