# 아기 상어
# i,j,상어크기,먹은갯수,걸린시간(초)
def can_eat(i, j, shark,):
    for f in range(len(fishes)):
        fi, fj, d, size = fishes[f]
        fishes[f][2] = abs(fi-i)+abs(fj-j)

    fishes.sort(key=lambda x:(x[2], x[0], x[1]))    # 가장 가깝고, 가장 위, 가장 왼쪽

    for fi, fj, d, size in fishes:
         if not visited[fi][fj] and size < shark and d > 0:
            print('.........................')
            print(f'다음 물고기 : {fi, fj,}, 상어 크기 : {shark} ')
            return fi, fj, shark
    
    return 0    # 먹을 물고기가 없다면 0반환

def bfs(i, j, shark, eat):
    global cnt, visited
    try:
        fi, fj, shark = can_eat(i, j, shark)    #잡아야할 물고기 위치 반환됨
    except TypeError:
        return

    que = [[i, j]]
    while que:
        si, sj = que.pop(0)
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and area[ni][nj] <= shark:
                visited[ni][nj] = visited[si][sj] + 1
                que.append([ni, nj])
                if [ni, nj] == [fi, fj]:
                    cnt += visited[ni][nj]
                    eat += 1
                    if eat == shark:
                        shark += 1
                        eat = 0
                    # print(f'초기화 이전 visited : ')
                    # for _ in range(N):
                    #     print(*visited[_])
                    # print('.........................')
                    isEaten.append([ni, nj])
                    for i in range(N):
                        for j in range(N):
                            if [i, j] not in isEaten:
                                visited[i][j] = 0
                            # else:
                            #     visited[i][j] = 1
                    
                    print(f'초기화 이후 visited : ')
                    for _ in range(N):
                        print(*visited[_])
                    print('.........................')
                    break
        if [ni, nj] == [fi, fj]:
            break

    bfs(ni, nj, shark, eat)

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
delta = [[-1,0],[0,-1],[1,0],[0,1]]

si = sj = 0
fishes = []
isEaten = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            si, sj = i, j
        elif 1 <= area[i][j] <= 6:
            fishes.append([i, j, 0, area[i][j]])  # i, j, 아기상어와의 거리, 물고기 크기
cnt = 0
bfs(si, sj, 2, 0)    # 상어 좌표, 크기, 먹은 개수

print(isEaten)
ansi, ansj = isEaten[-1]
print(visited[ansi][ansj])
