# 평범한 배낭
'''
10 15
1 1
2 3
5 3
5 1
4 5
3 3
3 2
4 4
4 4
4 3
'''
# 평범한 배낭
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

items = []
for _ in range(N):
    a, b = map(int, input().split())
    if a <= K:
        items.append((a,b))

# items.sort(key=lambda x:x[1], reverse=True)
items.sort(key=lambda x:(-x[1], x[0]))

# print(items)

from collections import deque
que = deque(items)

maxV = 0
while que:
    cap = K
    sumV = 0
    while cap > 0 and que:
        w, v = que.popleft()
        if w <= cap:
            sumV += v
            cap -= w
        else:
            que.appendleft((w,v))
            break

    if maxV < sumV:
        maxV = sumV

print(maxV)
