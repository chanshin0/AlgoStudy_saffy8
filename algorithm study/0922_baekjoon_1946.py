# 신입사원
import sys
T = int(sys.stdin.readline().strip())
for tc in range(T):
    N = int(sys.stdin.readline().strip())
    applicants= [[] for _ in range(N)]
    for n in range(N):
        sco1, sco2 = map(int, sys.stdin.readline().split())
        applicants[n] = [sco1, sco2]

    kill = [0]*N
    for i, j in applicants:
        for vi, vj in applicants:
            cnt = 0
            if [i, j] != [vi,vj]:
                if i > vi and j > vj:
                    kill[applicants.index([i, j])] += 1
                    break

    print(kill.count(0))