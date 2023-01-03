# 벽 부수고 이동하기

# 여기에 시작지점이랑 도착지점으로 각각 넣어서 인접한 칸에 벽이 몇줄인지 셀것임
def len_wall(i, j):
    if (i, j) == (0, 0):    # 시작 지점일 때
        if area[i][j+1] and area[i+1][j]:    # 만약 오른쪽 아래가 다 벽이면
            cnt = 0
            nj = j+1
            while nj < M and area[i][nj]:   # nj가 인덱스 벗어나거나 0나올때까지
                cnt += 1                    # 오른쪽 벽길이 ++
                nj += 1
            cnt2 = 0
            ni = i+1
            while ni < N and area[ni][j]:   # ni가 인덱스 벗어나거나 0나올때까지
                cnt2 += 1                   # 아래쪽 벽길이 ++
                ni +=1
            if cnt >= 2 and cnt2 >= 2:
                print(-1)
                exit(0)

from collections import deque
# 1. 일반적인 최단경로
def bfs(i, j):
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    que = deque([[i,j]])
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and not area[ni][nj]:
                visited[ni][nj] = visited[si][sj] + 1
                que.append([ni,nj])
                if (ni, nj) == (N-1,M-1):
                    return visited

from sys import stdin
N, M  = map(int, stdin.readline().split())
area = [list(map(int, input())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

ans = bfs(0, 0)
print(ans)