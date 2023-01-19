# 예산

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

left = 1
right = max(budgets)

maxV = 0
while left <= right:
    mid = (left+right)//2

    sumV = 0
    for b in budgets:
        if b < mid:
            sumV += b
        else:
            sumV += mid

    if sumV <= M:
        left = mid+1
        maxV = max(maxV, mid)
    else:
        right = mid-1
print(maxV)