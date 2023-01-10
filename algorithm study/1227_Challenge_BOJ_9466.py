# 텀 프로젝트
import sys
sys.setrecursionlimit(10**6)

def dfs(i,s):
    visited.append(choice[i])

    if choice[i] == i or visited[-1] == s or matching[choice[i]]:
        return
    else:
        dfs(choice[i],s)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    choice = [0]+list(map(int, input().split()))
    matching = [0]*(n+1)

    cnt = 0
    for s in range(1, n+1):
        if not matching[s]:
            visited = []
            dfs(s,s)
            if s != visited[-1]:
                cnt += 1
            else:
                for v in visited:
                    matching[v] = 1
    print(cnt)