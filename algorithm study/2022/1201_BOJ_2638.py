# 치즈

# 이건 그냥 dfs입니다.
def find_on_the_surface(i, j):
    for di, dj in delta:
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and not area[ni][nj]:
            visited[ni][nj] = 1
            find_on_the_surface(ni, nj)

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[0]*M for _ in range(N)]

# 포인트 1. 어차피 치즈는 가장자리에는 놓이지 않기 때문에, 가장자리 아무데서나 dfs 돌려버리면
# 모든 외곽의 공간을 방문처리할 수 있다.
visited[0][0] = 1
find_on_the_surface(0, 0)

t = 0
while True:
    cheese_melting = []                          # 1. 이번 턴에 녹는 치즈가 담길 리스트
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:                  # 2. 치즈자리에서 델타 탐색
                cnt = 0
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if visited[ni][nj] == 1:     # 3. 외곽의 공간 카운트
                        cnt += 1

                if cnt >= 2:                     # 4. 인접한 외곽이 2개 이상이면 녹일 리스트에 저장
                    cheese_melting.append((i, j))

    if not cheese_melting:                       # 5. [종료조건] 녹일 치즈가 없다면 종료.
        break
    else:
        for i,j in cheese_melting:               # 6. 녹일 치즈에 대해서 반복문 돌면서
            visited[i][j] = 1                    # 6-1. 외곽의 공간으로 만들고
            area[i][j] = 0                       # 6-2. 빈공간으로 만들고
            find_on_the_surface(i, j)            # 6-3. 혹시 내부 공간이 외곽으로 드러날 수 있으므로 dfs도 돌려준다.

    t += 1

print(t)