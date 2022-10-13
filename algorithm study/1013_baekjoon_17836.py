# 공주님을 구해라!
import sys
input = sys.stdin.readline
from collections import deque
def bfs(i, j, ei, ej):
    global gi, gj, ans2
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    que = deque([(i, j)])
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[si][sj] + 1
                que.append((ni, nj))
                if (ni, nj) == (ei, ej):                    # 공주 찾으면 최소거리 반환
                    return visited[ni][nj] - 1
                if area[ni][nj] == 2:                       # 탐색하다가 그람 찾으면 좌표와 최소거리를 저장
                    gi, gj = ni, nj
                    ans2 = visited[gi][gj] - 1
    return 10001                                            # 탐색 다 끝났는데 공주 못찾으면 INF값 반환

N, M, T = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

gi = gj = -1                                    # 그람 좌표값 담을 변수
ans2 = 0                                        # 시작위치부터 그람까지의 최소거리 담을 변수

ans = bfs(0, 0, N-1, M-1)                       # 1. 시작위치부터 공주위치까지 그냥 bfs

if gi != -1 and gj != -1:                       # 2-1. 만약 첫번째 bfs에서 그람을 찾았으면 ans와 ans2 최소비교
    ans2 += abs(N-1 - gi) + abs(M-1 - gj)           # 그람부터 공주까지 치트키
    if ans > ans2:
        ans = ans2

if ans <= T:                                    # 시간 내에 구할 수 있는지 여부 체크
    print(ans)
else:
    print('Fail')