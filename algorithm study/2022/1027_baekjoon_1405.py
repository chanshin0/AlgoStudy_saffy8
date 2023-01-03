# 미친로봇
def dfs(i, j, n, arr):

    if n == N:
        print(arr, end=' ')
        # [0, 0] [2, 0] [2, 1] [2, 2] [3, 0] [3, 1]
        return

    for d in range(4):
        di, dj = delta[d]
        ni,nj = i+di,j+dj
        if (ni,nj) not in visited:
            visited.append((ni,nj))
            arr.append(d)
            dfs(ni,nj, n+1, arr)
            visited.remove((ni,nj))
            arr.pop()
        else:
            return

N, e,w,s,n = map(int, input().split())
direc = [e,w,s,n]
delta = [[0,1],[0,-1],[1,0],[-1,0]]

visited = []
visited.append((0,0))
possible = 4**N
rst = []
dfs(0, 0, 0, [])
# print(rst)


