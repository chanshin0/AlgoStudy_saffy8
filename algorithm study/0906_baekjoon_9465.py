# 스티커
import sys
T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    # 최대값부터 쭉 내려오면서 델타를 0으로 만들다가, 모든 델타가 다 0이면 종료후 합계
    sumV = 0
    while True:
        row0 = max(sticker[0])
        row1 = max(sticker[1])
        if row0 > row1:
            target_idx = sticker[0].index(row0)
            sumV += row0
            if target_idx - 1 >= 0:
                sticker[0][target_idx-1] = 0
            if target_idx + 1 < n:
                sticker[0][target_idx+1] = 0
            sticker[1][target_idx] = 0
            sticker[0][target_idx] = 0

        else:
            target_idx = sticker[1].index(row1)
            sumV += row1
            if target_idx - 1 >= 0:
                sticker[1][target_idx - 1] = 0
            if target_idx + 1 < n:
                sticker[1][target_idx + 1] = 0
            sticker[0][target_idx] = 0
            sticker[1][target_idx] = 0
            if row0 == 0:
                if row1 == 0:
                    break
    print(sumV)

