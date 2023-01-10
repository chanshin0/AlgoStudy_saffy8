# 크게 만들기
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().strip()))

# [풀이 방법] 범위를 좁혀가면서 그 안에서 최대값을 계속 출력한다.

start = 0   # 시작 인덱스
t = N-K     # N-K자리 숫자를 출력할 것이다.

while t > 0:
    maxV = 0
    for i in range(start, N-t+1):   # "start부터 N-t까지 범위"에서 최대값을 찾아 자릿수를 다 채울때까지 출력한다.
        if num[i] > maxV:
            maxV = num[i]
            start = i+1
    t -= 1
    print(maxV, end='')
