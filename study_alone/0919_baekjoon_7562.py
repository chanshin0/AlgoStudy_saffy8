# 나이트의 이동
def bfs(i, j):
    if [i, j] == [ei, ej]:
        return 0
    else:
        que = [[i, j]]
        while que:
            fi, fj = que.pop(0)
            for di, dj in delta:
                ni = fi+di
                nj = fj+dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    que.append([ni, nj])
                    visited[ni][nj] = visited[fi][fj] + 1
                    if [ni, nj] == [ei, ej]:
                        return visited[ni][nj]
                    # print(visited[end[0]][end[1]])




from sys import stdin
T = int(stdin.readline())
for tc in range(T):
    N = int(stdin.readline())
    si, sj = map(int, stdin.readline().split())
    ei, ej = map(int, stdin.readline().split())

    delta = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
    visited = [[0]*N for _ in range(N)]

    print(bfs(si, sj))


