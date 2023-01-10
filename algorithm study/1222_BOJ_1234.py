# 크리스마스 트리
from itertools import combinations

N, r, g, b = map(int, input().split())

tree = list(range(1, N+1))

ans = 0
for level in range(1, N+1):
    temp = list(combinations([r,g,b], level))
    for i in temp:
        if i:
            ans += 1


print(ans)