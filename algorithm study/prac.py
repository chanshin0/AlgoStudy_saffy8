<<<<<<< HEAD
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().strip()))

k = 9
maxV = 0
temp = 0
while temp < N-K:
    if maxV < num.count(k):
        maxV = k
    temp += num.count(k)
    k -= 1
print(temp)
print(k)
print(num.index(maxV-1))

for i in range(N):
    if num[i] > k:
        print(num[i], end='')
=======
>>>>>>> 9e74a37ae6a24c63cce251a30f0d0a7d975c0d16
