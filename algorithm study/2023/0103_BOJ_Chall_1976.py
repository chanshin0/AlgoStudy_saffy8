n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
routes = list(map(int, input().split()))
for r in range(m):
    routes[r] -= 1

def bfs(i,e):
    visited = [0]*n
    que = [i]
    visited[i] = 1
    while que:
        s = que.pop(0)
        for j in range(n):
            if arr[s][j] and not visited[j]:
                if j == e:
                    return 1
                visited[j] = 1
                que.append(j)
    return 0

ans = "YES"
for i in range(m-1):
    if routes[i] == routes[i+1]:
        continue
    rst = bfs(routes[i], routes[i+1])
    # print(rst, routes[i], routes[i+1])
    if not rst:
        ans = "NO"
        break
print(ans)