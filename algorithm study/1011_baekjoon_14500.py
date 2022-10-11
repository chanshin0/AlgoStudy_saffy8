# 테트로미노
def dfs(i, j, d, sum):
    global ans

    # 남은 칸에 전부 최대값 더해도 현재 ans보다 작다면 더 볼 필요 없음
    if (maxV*(4-d))+sum < ans:
        return

    # 4칸 되면 최대값 비교 후 종료
    if d == 4:
        if ans < sum:
            ans = sum
        return

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
            if d == 2:
                visited[(ni, nj)] = 1
                dfs(i, j, d+1, sum+area[ni][nj])
                visited.pop((ni, nj))

            visited[(ni, nj)] = 1
            dfs(ni, nj, d+1, sum+area[ni][nj])
            visited.pop((ni, nj))

from sys import stdin
N, M = map(int, stdin.readline().split())
area = [list(map(int, stdin.readline().split())) for _ in range(N)]
delta = [[0,1],[1,0],[0,-1],[-1,0]]

ans = 0
maxV = max(map(max, area))
visited = {}
for i in range(N):
    for j in range(M):
        visited[(i, j)] = 1
        dfs(i, j, 1, area[i][j])
        visited.clear()
print(ans)

