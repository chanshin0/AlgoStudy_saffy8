# 집합의 표현
from sys import stdin
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    if x < y:
        rep[find_set(y)] = find_set(x)
    else:
        rep[find_set(x)] = find_set(y)

n, m = map(int, stdin.readline().split())

rep = list(range(n+1))
for _ in range(m):
    c, a, b = map(int, stdin.readline().split())
    if not c:
        union(a, b)
    elif c:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 7 3
'''