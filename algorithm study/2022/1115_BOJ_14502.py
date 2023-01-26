# 연구소
from collections import deque

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

# 겁나 포괄적인 벽조건
# 1. 벽 or 바이러스 or 직사각형의 변과 인접해있다.

# 안전영역 구하는 함수
visited = [[0]*M for _ in range(N)]
# 선택한 벽 3개 visited 처리 후 진입
def bfs(i, j):
    cnt = 0
    que = deque([(i,j)])
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni,nj = si+di,sj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                cnt += 1
                visited[ni][nj] = 1
                que.append((ni,nj))
    return cnt
visited[0][1] = 1
visited[1][0] = 1

print(bfs(0,0))
