# 1,2,3 더하기
def perm(n, k, r):
    if n == k:
        # s = 0
        # for i in range(k):
        #
        print(p)
    else:
        for i in range(l):
                p[n] = nums[i]
                perm(n+1, k, l)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = [1,2,]
    l = len(nums)
    p = [0]*n
    used = [0]*n
    perm(0, n, l)

