# 최대힙
from sys import stdin
T = int(stdin.readline())
arr = [0]
for tc in range(T):
    x = int(stdin.readline())
    if x == 0:
        if arr:
            print(arr.pop(0))
            arr.append(x)
        else:
            print(0)
    else:
        if arr:
            