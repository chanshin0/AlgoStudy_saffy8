# 1,2,3 더하기
def perm(n, k, r):
    global cnt
    # 종료조건 1. 0이 2개 이하이고, 합이 n
    if p.count(0) <= 2 and sum(p) == N:
        cnt += 1
    if n == k:
        return
    # 종료조건 2. 합이 n을 넘어가면
    if sum(p) > N:
        return
    else:
        for i in range(r):
            p[n] = nums[i]
            perm(n+1, k, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [1,2,3]
    l = len(nums)
    p = [0]*N
    used = [0]*N
    cnt = 0
    perm(0, N, l)   # l개중에 N개 뽑는 순열
    print(cnt)
