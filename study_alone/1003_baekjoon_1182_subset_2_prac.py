# 부분수열의 합
# 직접 써본것
def f(i, N):
    global cnt
    if i == N:          # 비트를 끝까지 다 채웠음
        s = 0
        for i in range(N):
            if bit[i]:
                s += nums[i]
        if s == S:
            cnt +=1

    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

from sys import stdin
N, S = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
l = len(nums)
bit = [0]*l
cnt = 0
f(0, l)
print(cnt)
# 1, 63