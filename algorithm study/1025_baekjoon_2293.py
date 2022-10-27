# 동전 1
n, k = map(int, input().split())
arr = []
cnt = 0
for _ in range(n):
    c = int(input())
    arr += list(range(c,k+1,c))

arr = set(arr)
# print(arr)
for i in arr:
    if k-i in arr or k==i:
        cnt += 1
print(cnt)
