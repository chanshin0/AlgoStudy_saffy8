# 자료구조는 정말 최고야
from sys import stdin
N, M = map(int, stdin.readline().split()) # 4 2

for i in range(M):
    n = int(stdin.readline().strip())
    dummys = list(map(int, stdin.readline().split()))
    for j in range(n-1):
        if dummys[j] < dummys[j+1]:
            print('No')
            exit(0)

print('Yes')

