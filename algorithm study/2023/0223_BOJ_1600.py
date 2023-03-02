# 말이 되고픈 원숭이
from collections import deque
K = int(input())
W, H = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(H)]
# print(area)
delta = [[0,1],[1,0],[0,-1],[-1,0]]
h_delta = [[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

def bfs(i, j):
    visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]
    visited[0][0][0] = 1
    que = deque([(0,0,0)])
    # t = 1
    while que:
        si, sj, k = que.popleft()

        if (si,sj) == (H-1,W-1):
            return visited[k][si][sj] - 1

        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < H and 0 <= nj <W and area[ni][nj] == 0 and not visited[k][ni][nj]:
                visited[k][ni][nj] = visited[k][si][sj] +1
                que.append((ni,nj,k))

        if k < K:
            for di, dj in h_delta:
                ni, nj = si + di, sj + dj
                if 0 <= ni < H and 0 <= nj < W and area[ni][nj] == 0 and not visited[k+1][ni][nj]:
                    visited[k+1][ni][nj] = visited[k][si][sj] +1
                    que.append((ni, nj, k+1))

        # print(f'{t}번째.{si,sj, k}...........')
        # for i in range(K):
        #     for j in range(H):
        #         print(visited[i][k])
        # print('.....................')
        # t += 1
    return -1

ans = bfs(0,0)
print(ans)
