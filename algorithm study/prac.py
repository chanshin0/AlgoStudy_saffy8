# 하나로
def dijk(s):
    d[s] = 0  # 시작정점 0처리

    for _ in range(N):
        u = 0
        minV = 1000000000001  # 0~N-1까지 정점 중 d[i]값이 최소인 정점u를 찾는다
        for i in range(N):
            if minV > d[i] and not visited[i]:
                minV = d[i]
                u = i

        visited[u] = 1
        for j in range(N):  # 정점 u부터 나머지 섬과의 거리를 갱신해준다.
            if not visited[j]:
                leng = (lo_x[u] - lo_x[j]) ** 2 + (lo_y[u] - lo_y[j]) ** 2
                d[j] = min(d[j], E * leng)

    return round(sum(d))


T = int(input())
for tc in range(T):
    N = int(input())
    lo_x = list(map(int, input().split()))
    lo_y = list(map(int, input().split()))
    E = float(input())

    d = [1000000000001] * N
    visited = [0] * N

    print(f'#{tc + 1} {dijk(0)}')