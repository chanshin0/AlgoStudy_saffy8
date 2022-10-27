# 로봇청소기
from sys import stdin
input = stdin.readline

while True:
    w, h = map(int, input().split())
    if (w,h) == (0,0):
        break
    else:
        room = [list(input().strip()) for _ in range(h)]
        delta = [[0,1],[1,0],[0,-1],[-1,0]]
        cnt = 0

        dirties = []
        si=sj=0
        for i in range(h):
            for j in range(w):
                if room[i][j] == '*':
                    dirties.append([i, j, 0])
                if room[i][j] == "o":
                    si, sj= i, j

        # 1. 현재 위치에서 가장 가까운 쓰레기를 찾고, 거리를 cnt에 더하고, 좌표를 반환하는 함수
        def next_dirty(si,sj):
            global cnt
            minV = w*h
            mi=mj=0
            for x in range(len(dirties)):
                i,j,d = dirties[x]
                # if abs(si-i)+abs(sj-j) < minV:
                #     minV = abs(si-i)+abs(sj-j)
                #     mi, mj=i,j
                minD = bfs(si,sj,i,j)
                if minD:
                    dirties[x][2] = minD
                else:
                    return
            dirties.sort(key=lambda x:x[2])
            cnt += dirties[0][2]
            mi,mj = dirties[0][0],dirties[0][1]
            dirties.pop(0)
            return (mi,mj)


        # 2. (i,j)부터 (mi,mj)까지의 최소거리 계산하는 함수
        def bfs(i,j,mi,mj):
            global cnt
            visited = [[0]*w for _ in range(h)]
            visited[i][j] = 1

            que = [(i,j)]
            while que:
                si, sj = que.pop(0)
                for di, dj in delta:
                    ni,nj=si+di,sj+dj
                    if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and room[ni][nj] != "x":
                        visited[ni][nj] = visited[si][sj] + 1
                        que.append((ni,nj))
                        if (ni,nj) == (mi, mj):
                            # dirties.remove((mi,mj))
                            # cnt += visited[ni][nj]-1
                            return visited[ni][nj]-1

            if not visited[mi][mj]:
                return 0


        rst = 1
        while dirties:
            try:
                mi, mj = next_dirty(si,sj)
            except TypeError:
                rst = 0
                break
            si,sj = mi,mj

        if rst:
            print(cnt)
        else:
            print(-1)
