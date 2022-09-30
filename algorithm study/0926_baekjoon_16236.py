# 아기 상어
# i,j,상어크기,먹은갯수,걸린시간(초)
def dfs(i, j, shark, eat, s_cnt):
    global shark_cnt
    if shark_cnt == s_cnt:
        return

    visited[i][j] = 1

    for f in range(len(fishes)):
        fi, fj, d, size = fishes[f]
        fishes[f][2] = abs(fi-i)+abs(fj-j)

    fishes.sort(key=lambda x:(x[2], x[0], x[1]))    # 가장 가깝고, 가장 위, 가장 왼쪽

    for fi, fj, d, size in fishes:
         if not visited[fi][fj] and size < shark and d > 0:
             bfs(i, j, fi, fj, shark)
             eat += 1
             if eat == shark:
                 shark += 1
                 eat = 0
             dfs(fi, fj, shark, eat, s_cnt+1)
             return

def bfs(i, j, fi, fj, shark):
    global cnt, visited
    que = [[i, j]]
    while que:
        si, sj = que.pop(0)
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and area[ni][nj] <= shark:
                visited[ni][nj] = visited[si][sj] + 1
                que.append([ni, nj])
                if [ni, nj] == [fi, fj]:
                    cnt += visited[ni][nj] - 1
                    visited = [[0]*N for _ in range(N)]
                    return

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
delta = [[-1,0],[0,-1],[1,0],[0,1]]

shark_cnt = 0
si = sj = 0
fishes = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            si, sj = i, j
        elif 1 <= area[i][j] <= 6:
            fishes.append([i, j, 0, area[i][j]])  # i, j, 아기상어와의 거리, 물고기 크기
            shark_cnt += 1
cnt = 0
dfs(si, sj, 2, 0, 0)
print(cnt)
