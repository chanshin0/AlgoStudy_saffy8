# 반도체 설계
def binary(target):
    left = 1
    right = L - 1
    while left <= right:
        mid = (left + right) // 2

        if ans[mid] == target:
            break
        elif ans[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


n = int(input())
arr = list(map(int, input().split()))
L = len(arr)

ans = [arr[0]]

for i in range(1,n):
    if ans[-1] < arr[i]:
        ans.append(arr[i])
    else:
        for j in range(len(ans)):
            if ans[j]


5 6 7 1 2