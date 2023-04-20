# 콘센트
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

time = 0
concent = []

# [1]. 콘센트에 전자기기를 전부 낄 때까지 걸리는 시간을 구하는 반복문.
while arr:
    # [1-1]. 콘센트가 꽉차거나, 전자기기가 없을 때까지 꼽음.
    while len(concent) < M and len(arr)>0:
        concent.append(arr.pop())
    concent = sorted(concent, reverse=True)

    # [1-2]. (정렬) 젤 뒤에있는 기기(fast)가 젤 빨리 충전 끝남. 그 시간만큼 흘렀다고 가정.
    fast = concent[-1]
    time += fast

    # [1-3]. 콘센트를 뒤에서 부터 순회하면서 어디까지 충전 다 되었는지 체크
    tagetId = -1
    for i in range(len(concent)-1, -1, -1):
        concent[i] -= fast
        if concent[i] == 0:
            tagetId = i

    # [1-4]. 충전 다 된 기기들 버리고 자름. 이후 1~4 반복.
    concent = concent[:tagetId]

if (concent):
    time += max(concent)
print(time)

