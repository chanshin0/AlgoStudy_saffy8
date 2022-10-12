# 뱀과 사다리 게임
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
lucky = []
trap = []
for _ in range(N):
    u, v = map(int, stdin.readline().split())
    lucky.append((u, v))
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    trap.append((u, v))

# maxV = max(map(max, lucky))
# minV = min(map(min, lucky))
cnt = 1
ismax = 0
i = j = 0
for u, v in lucky:
    if v-u > ismax:
        ismax = v-u
        i, j = u, v

cnt += (i-2)//6
while lucky:
    u, v = lucky.pop()
    if 100-v <= 6:
        cnt += 1
    if v < j:
        continue
    else:
        if v-u > 6:



print(lucky)

