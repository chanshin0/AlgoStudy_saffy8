# 입국심사
N, M = map(int, input().split())
immigrations = [int(input()) for _ in range(N)]
maxM = 1000000000
maxT = 1000000000

left = 0
right = maxT*maxM//N+1

minV = maxT*M
while left <= right:
    mid = (left+right)//2
    cnt = 0

    for i in immigrations:
        cnt += mid//i
        if cnt > M:
            break

    if cnt < M:
        left = mid+1
    # elif cnt > M:
    #     # 통과한 사람이 더 많으면 : 시간범위를 줄임
    #     right = mid-1
    # 얘를 주석하니까 통과됐는데 왜그럴까
    else:
        # 일치하면 최소값 갱신하고 시간범위를 줄임
        minV = min(mid,minV)
        right = mid -1

print(minV)
