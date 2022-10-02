# 최소 이동거리
def dijk(s, n): # 시작정점, 정점의 개수
    d[0] = 0

    for i in range(n):                                 # n개의 정점 탐색
        for j in range(n):                             # 정점 i와 인접한 정점 j에 대해서
            if adjM[i][j]:                             # 인접 정점 맞다면
                d[j] = min(d[j], d[i] + adjM[i][j])    # j까지의 최단거리 갱신



# from sys import stdin
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adjM[a][b] = c

    INF = 11
    d = [INF]*(N+1)
    dijk(0, N+1)
    print(f'#{tc} {d[N]}')