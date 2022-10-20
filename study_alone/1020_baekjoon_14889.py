# 스타트와 링크
def ncr(n, r, s):
    global ismin

    if r == 0:
        teamA = 0
        for i in comb:
            for j in comb:
                if power[i][j]:
                    teamA += power[i][j]
        rest = []
        for i in range(n):
            if i not in comb:
                rest.append(i)
        teamB = 0
        for i in comb:
            for j in comb:
                if power[i][j]:
                    teamB += power[i][j]
        if abs(teamA-teamB) < ismin:
            ismin = abs(teamA-teamB)

    else:
        for i in range(s, n-r+1):
            comb[r-1] = members[i]
            ncr(n, r-1, i+1)


N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]

# N개 중에 N//2개 뽑
ismin = sum(map(sum, power))
members = list(range(N))
comb = [0]*(N//2)
ncr(N, N//2, 0)
print(ismin)