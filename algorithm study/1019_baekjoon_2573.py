# 빙산
def check(i, j):
    global is_divided

    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            try:
                if (ni, nj) in new_ice:
                    visited[ni][nj] = 1
                    is_divided -= 1
                    # print(visited, cnt)
                    check(ni, nj)
            except NameError:
                if area[ni][nj] != 0:
                    visited[ni][nj] = 1
                    is_divided -= 1
                    # print(visited, cnt)
                    check(ni, nj)

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

ice_bergs = {}
mi = mj = ice = 0
for i in range(N):
    for j in range(M):
        if area[i][j] != 0:
            ice_bergs[(i,j)] = area[i][j]
            ice += 1
            mi, mj = i, j

if not ice:
    print(0)
else:
    visited = [[0] * M for _ in range(N)]
    visited[mi][mj] = 1
    is_divided = ice - 1
    check(mi, mj)

    if is_divided:
        print(0)
        exit(0)

    cnt = 1
    while True:

        # 녹이기
        for i, j in ice_bergs:
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and area[ni][nj] == 0:
                    ice_bergs[(i, j)] -= 1
                    if ice_bergs[(i, j)] == 0:
                        break

        # 다 녹을 때까지 돌았으면 0
        if not ice_bergs:
            print(0)
            break

        # 빙산이 있다면
        else:
            # 아직 남아있는 빙산 새로 담기
            new_ice = {}
            mi = mj = 0
            for i, j in ice_bergs:
                if ice_bergs[(i, j)] == 0:
                    pass
                else:
                    new_ice[(i, j)] = ice_bergs[(i, j)]
                    mi, mj = i, j
            # print(new_ice, cnt)

            # 빙산이 한 덩어리인지 check
            visited = [[0]*M for _ in range(N)]
            visited[mi][mj] = 1
            is_divided = len(new_ice) - 1
            check(mi, mj)

            # 나뉘어졌는지 여부 확인
            if is_divided:
                if is_divided < 0:
                    print(0)
                else:
                    print(cnt)
                exit(0)
            else:
                cnt += 1
                continue

