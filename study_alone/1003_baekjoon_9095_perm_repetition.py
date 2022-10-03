# 1,2,3 더하기
def perm(n, k, r):  # n번째 자리를 구한다, 순열의 크기 k, r은 순열을 만들 배열의 크기
    global cnt
    # 가지치기 종료조건 1. 현재 결정된 순열의 합이 2자리 이상이면서, 합계가 N이면 종료
    if n > 0 and sum(p[:n]) == N:
        cnt += 1
        return
    # 기본 종료조건. 모든 자리 순열이 다 결정되면 종료
    if n == k:
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
    perm(0, N, l)   # l개중에 N개 뽑는 중복순열
    print(cnt)
