#  미로탐색
from sys import stdin
N, M = map(int, stdin.readline().split())
miro = [list(map(int, stdin.readline().strip())) for _ in range(N)]

delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[0]*M for _ in range(N)]

queue = [[0,0]]
while queue:                # 더 이상할 탐색할 칸이 없을 때까지
    i, j = queue.pop(0)
    visited[i][j] = 1
    for di, dj in delta:
        ni = i+di
        nj = j+dj
        if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] == 1 and visited[ni][nj] == 0:
            queue.append([ni,nj])
            miro[ni][nj] = miro[i][j] + 1
            if [ni, nj] == [N, M]:
                break

print(miro[N-1][M-1])
