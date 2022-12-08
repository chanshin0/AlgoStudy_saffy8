# 연구소 2

def bfs(i, j):
    visited[i][j] = 1

    que = [(i,j)]
    while que:
        si,sj = que.pop(0)
        for di,dj in delta:
            ni,nj = si+di,sj+dj
            # 조건 1. 벽이 아니라면 일단 진입
            if 0<=ni<N and 0<=nj<N and area[ni][nj] != 1:
                # 조건 2-1. 한번도 방문하지 않은 곳이라면
                if visited[ni][nj] == 0:
                    # 방문한 곳에서 +1초
                    visited[ni][nj] = visited[si][sj] + 1
                    que.append((ni, nj))

                # 조건 2-2. 방문한 적이 있는 곳이라면
                else:
                    # 조건 3-1. 최소 시간이 갱신될 때만 진입
                    if visited[ni][nj] > visited[si][sj] + 1:
                        visited[ni][nj] = visited[si][sj] + 1
                        que.append((ni, nj))


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

from itertools import combinations

walls = []
can_put = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 2:
            can_put.append((i,j))
        elif area[i][j] == 1:
            walls.append((i,j))

viruses = list(combinations(can_put, M))

results = []
for t in range(len(viruses)):
    rst = 0
    # 포인트 1. visited를 여기서 초기화
    visited = [[0] * N for _ in range(N)]

    # 이렇게 bfs를 돌리고 나면 visited가 싹 깔림
    for ti, tj in viruses[t]:
        bfs(ti, tj)

    # 포인트 2. 방문 못한 곳이 있는지 확인하기 위해서 일단 벽을 싹 1처리 해버림.
    for wi, wj in walls:
        visited[wi][wj] = 1

    # 그 이후에도 visited에 0이 남아 있다면 방문 못한 것임
    if min(map(min, visited)) == 0:
        # 결과는 -1
        rst = -1

    else:
        # 방문 못한 곳이 없다면 최소 시간을 rst에 저장
        rst = max(map(max, visited)) - 1

    # 비교를 위해 rst값을 리스트에 저장
    results.append(rst)

minV = 2500
for ans in results:
    if ans != -1:
        # 포인트 3. -1이 아닌 결과에 대해서만 최소값 계산
        if minV > ans:
            minV = ans

# 출력. 모든 ans가 -1이었다면 minV에는 2500이 남아있을 것이므로 조건설정 후 출력
print(-1) if minV == 2500 else print(minV)
