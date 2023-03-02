# 멀티탭 스케줄링
N, K = map(int, input().split())
sequence = list(map(int, input().split()))

from collections import deque
que = deque(sequence)
multitap = deque([])
cnt = 0
while que:
    # print(multitap, cnt)
    now = que.popleft()
    if len(multitap) < N:
        multitap.append(now)
    else:
        if now in multitap:
            pass
        else:
            # 멀티탭에 꽂히지 않은 애 차례면 누굴 뽑을지 정해야함
            priority = [0]*len(multitap)
            for i in range(len(multitap)-1,-1,-1):
                if multitap[i] in que:
                    priority[i] += 1
            target = priority.index(min(priority))
            multitap[target] = now
            cnt += 1
print(cnt)

'''
2 8
1 2 3 4 3 4 2 2
'''
