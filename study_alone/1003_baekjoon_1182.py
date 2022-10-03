# 부분수열의 합
from sys import stdin
N, S = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
l = len(nums)

cnt = 0
for i in range(1<<l):               # l개의 비트를 가지면 0101...찍히는 경우의 수는 2**l개
    temp = []
    for j in range(l):              # 모든 비트칸에 대해서
        if i & (1<<j):              # i의 j번 비트가 1이면
            # temp.append()         # j번 비트 칸에 들어있는 숫자 출력
            temp.append(nums[j])

    # 비트 i가 가리키는 모든 원소가 temp에 담김
    if len(temp) > 0:               # 문제 조건
        if sum(temp) == S:
            cnt += 1

print(cnt)