# 2021 KAKAO BLIND RECRUITMENT 합승 택시 요금
# fares = 	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# n = 6
# s = 4
# a = 6
# b = 2
# ans = 0
# INF = 100000*n

def dijk(s, N, visited, costs, INF, adjM):

    # [pyjune의 전술노트 복습]
    costs[s] = 0                                        # 1. 시작정점의 최소비용은 0

    for _ in range(N - 1):                              # 2. 시작정점(최소비용이 0으로 이미 결정됨)을 제외한 나머지 N-1개의 정점에 대한 최소비용을 구할 것이다.
        u = 0                                               # 2-1. 최소비용이 확정된 정점 u를 거점으로 하여 찾을 것이다.
        minV = INF
        for i in range(1, N + 1):                           # 2-2. 모든 정점을 돌면서
            if costs[i] < minV and not visited[i]:          # 2-3. 이전for문에 갱신된 최소비용이 가장 작은 u를 선택
                u = i
                minV = costs[i]

        visited[u] = 1                                  # 3. 선택한 정점 u는 최소비용이 결정되었음. 방문처리.

        for i in range(1, N + 1):                       # 4. 이 거점 u에서 다시 모든 정점을 돌며
            if adjM[u][i] != 0 and not visited[i]:          # 4-1. 정점 u와 i 사이에 간선이 있고, 최소비용이 아직 확정되지 않은 정점 i일 때,
                if costs[i] > costs[u] + adjM[u][i]:        # 4-2. 정점 i의 최소비용 갱신을 시도한다.
                    costs[i] = costs[u] + adjM[u][i]

                                                        # 5. N-1번 반복하면 시작정점으로부터 모든 정점의 최소비용이 결정됨

def solution(n, s, a, b, fares):

    # [솔루션]
    INF = 100000 * n                                    # INF 값 낭낭하게 설정
    adjM = [[0] * (n + 1) for _ in range(n + 1)]

    for start, e, c in fares:                           # 인접행렬에 양방향으로 가중치를 저장해 줌
        adjM[start][e] = c
        adjM[e][start] = c
                                                        # [생각 1]. 일단, 기준이 되는 a,b,s 세 정점에 대해서 최소비용을 계산한다.
    costs = [INF] * (n + 1)
    visited = [0] * (n + 1)
    dijk(s, n, visited, costs, INF, adjM)                   # 1-1. 데이크스트라를 돌리면 시작 정점 s로부터의 최소비용이 costs에 기록된다
    print(costs)

    costs_a = [INF] * (n + 1)
    visited_a = [0] * (n + 1)
    dijk(a, n, visited_a, costs_a, INF, adjM)               # 1-2. 마찬가지로 도착정점 a로부터의 최소비용이 costs_a에 담긴다.

    costs_b = [INF] * (n + 1)
    visited_b = [0] * (n + 1)
    dijk(b, n, visited_b, costs_b, INF, adjM)               # 1-3. 마찬가지로 도착정점 b로부터의 최소비용이 costs_b에 담긴다.

    print(costs_a)
    print(costs_b)

    answer = INF                                        # [생각 2]. 합승을 시도할 수 있는 기준점은 모든 정점에서 '시작 정점 s 그리고, s와 연결되지 않은 정점들'을 제외한 나머지 정점들이다.
    for i in range(1, n + 1):
        if i != s and costs[i] != INF:
            temp = costs[i] + costs_b[i] + costs_a[i]
                                                        # [생각 3]. 합승을 시도할 어떤 거점 i에 대한 최소합승비용 == costs[i] + costs_b[i] + costs_a[i]이다.
            if temp < answer:
                answer = temp

    if costs[a] + costs[b] < answer:                    # [생각 4]. 마지막으로 합승을 하지 않는 경우와 비교해 준다.
        answer = costs[a] + costs[b]

    return answer