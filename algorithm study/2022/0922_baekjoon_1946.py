# 신입사원
import sys
T = int(sys.stdin.readline().strip())
for tc in range(T):
    N = int(sys.stdin.readline().strip())
    paper = [0]*(N+1)
    interview = [0]*(N+1)
    for n in range(1, N+1):
        sco1, sco2 = map(int, sys.stdin.readline().split())
        paper[n] = sco1
        interview[n] = sco2

    ans = N
    for i in range(1, N):
        a = paper.index(max(paper[1:]))
        if interview[a] != 1:
            ans -= 1
            paper[a] = 0
            interview[a] = 0
        else:
            paper[a] = 0
            interview[a] = 0
    print(ans)


