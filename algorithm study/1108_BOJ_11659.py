# 구간 합 구하기 4
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
numbers = [0]+list(map(int, input().split()))
cumcumative_sum = [0]*(N+1)
for i in range(1,N+1):
    cumcumative_sum[i] = cumcumative_sum[i-1]+numbers[i]
# print(cumcumative_sum)

for _ in range(M):
    i, j = map(int, input().split())
    print(cumcumative_sum[j]-cumcumative_sum[i-1])