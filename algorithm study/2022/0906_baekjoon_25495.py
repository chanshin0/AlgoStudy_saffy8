# 에어팟
import sys
N = int(sys.stdin.readline())
phones = list(map(int, sys.stdin.readline().split()))
battery = [2]+[0]*(N-1)    # 배터리 소모량 담을 변수
new_idx = 0
# 배터리 소모량이 100을 넘어서초기화 될 떄의 인덱스

for i in range(1, N):
    # 앞 뒤가 같으면 직전 소모량 * 2, 초기화 된 상태면 그냥 2
    if phones[i-1] == phones[i]:
        battery[i] = battery[i-1]*2
        if battery[i] == 0:
            battery[i] = 2
    # 앞 뒤 다른 새로운 연결이면 2
    else:
        battery[i] = 2

    # 현재 누적 소모량 = 초기화 된 시점부터 i까지의 합계
    current = sum(battery[new_idx:i+1])
    # 커렌트가 100넘으면 초기화 하고, idx값 저장
    if current >= 100:
        battery[i] = 0
        new_idx = i

print(sum(battery[new_idx:]))
