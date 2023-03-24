# 덩치
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
rankings = [1]*N
for i in range(N):
    w, h = arr[i]                       # 나
    for j in range(N):
        if j==i: continue
        compareW, compareH = arr[j]     # 나랑 비교할 상대방
        if w<compareW and h<compareH:
            rankings[i] +=1             # 나보다 덩치크면 내 랭킹++
print(*rankings)