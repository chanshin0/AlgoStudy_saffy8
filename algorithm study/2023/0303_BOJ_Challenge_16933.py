# 벽 부수고 이동하기 3
from sys import stdin
from collections import deque

def bfs(i, j, k, d):
    visited[k][i][j] = 1
    que = deque([(i, j, k, d)])
    while que:
        si, sj, k, day = que.popleft()

        if (si, sj) == (N-1,M-1):
            return visited[k][si][sj]

        # [조건 1] 낮일 때 : 벽 부수기 가능
        if day:
            for di,dj in delta:
                ni,nj = si+di, sj+dj
                if 0 <= ni < N and 0 <= nj < M and not visited[k][ni][nj] and not area[ni][nj]:
                    visited[k][ni][nj] = visited[k][si][sj] + 1
                    que.append((ni,nj,k, not day))
            if k < K:
                for di, dj in delta:
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < M and not visited[k+1][ni][nj]:
                        visited[k+1][ni][nj] = visited[k][si][sj] + 1
                        que.append((ni, nj, k+1, not day))

        # [조건 2]밤일 때 : 벽 부술 수 없음
        else:
            flag = 1
            for di, dj in delta:
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[k][ni][nj]:
                    # [조건 2-1]벽이 아닌 곳은 하던대로 이동
                    if not area[ni][nj]:
                        visited[k][ni][nj] = visited[k][si][sj] + 1
                        que.append((ni, nj, k, not day))
                    # [조건 2-2]벽인 곳은 제자리 머무름
                    else:
                        que.append((si,sj,k,not day))
                        flag = 0
            # [조건 3] 제자리 머물렀으면 현재칸 visited += 1
            if not flag:
                visited[k][si][sj] += 1

    return -1

N, M, K = map(int, input().split())
area = [list(map(int, input())) for _ in range(N)]

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K+1)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]
ans = bfs(0,0,0,True)
print(ans)