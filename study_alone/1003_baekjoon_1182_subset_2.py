# 부분수열의 합
def f(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N:
        s = 0                   # 부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += nums[i]
        if s == S:
            if sum(bit):
                answer += 1         # 부분집합의 합이 10인 경우의 수

    else:
        bit[i] = 1              # A[i]가 부분집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

from sys import stdin
N, S = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
l = len(nums)
bit = [0]*l
answer = 0
cnt = 0
f(0, l)
print(answer)
# 1, 63