n = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
for i in range(2, n):
    if arr[i] < 2:
        continue

    for j in range(i):
        if arr[i] - arr[j] in arr[:i]:
            cnt += 1
            break

print(cnt)
