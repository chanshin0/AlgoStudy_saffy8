# 뮤탈리스크

N = int(input())
scv = list(map(int, input().split()))
destroyed = [0]*(N)
dp = [0]*61

que = [0]
while scv:
    t = que.pop(0)

    for i in [1,3,9]:
        if t+i <= 60:
            dp[t+i] = dp[t] + 1
            que.append(t+i)

    if N == 1:
        if dp[scv[0]]:
            print(dp[scv[0]])
            break
    elif N == 2:
        if dp[scv[0]] and dp[scv[1]]:
            print(max(dp[scv[0]], dp[scv[1]]))
            break
    else:
        if dp[scv[0]] and dp[scv[1]] and dp[scv[2]]:
            print(max(dp[scv[0]], dp[scv[1]], dp[scv[2]]))
            break





