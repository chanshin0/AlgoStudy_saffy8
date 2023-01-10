# 양팔저울
from sys import stdin
N = int(stdin.readline())
choos = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
beads = list(map(int, stdin.readline().split()))

dp = [choos.pop(0)]
for choo in choos:

    for i in range(len(dp)):
        if choo + dp[i] not in dp:
            dp.append(choo+dp[i])
        if abs(choo-dp[i]) not in dp:
            dp.append(abs(choo-dp[i]))

    if choo not in dp:
        dp.append(choo)

for bead in beads:
    if bead in dp:
        print('Y', end=' ')
    else:
        print('N', end=' ')