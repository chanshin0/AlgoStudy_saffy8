# 트럭
import sys
n, w, L = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))

cnt = 0             # 단위 시간 계산할 변수
bridge = [0]*w      # 다리

while truck:        # 트럭이 다 지나갈 때까지 반복문.
    front = truck.pop(0)    # 맨 앞 트럭
    rear = w-1              # 다리의 첫 진입점(리스트 맨뒤)
    if sum(bridge[1:])+front <= L:    # 진입 가능하면
        for i in range(1, w):
            bridge[i-1] = bridge[i]     # 앞으로 하나씩 밀고
        bridge[rear] = front            # 트럭 진입
        cnt += 1                        # 단위시간 +1

    else:                             # 진입 불가능 하면
        for i in range(1, w):
            bridge[i-1] = bridge[i]     # 앞으로 하나씩 밀고
        bridge[rear] = 0                # 한칸씩 밀었으니까 진입점 0
        truck = [front] + truck         # 트럭 대기
        cnt += 1                        # 단위 시간 +1

print(cnt+w)        # 반복문 끝나면 맨 마지막 트럭이 진입상태이므로 + w하고 출력