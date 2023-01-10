# 전봇대
import sys
N = int(sys.stdin.readline())
power_cord = [[] for _ in range(N)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a < b:
        power_cord[i] += list(range(a, b+1))
    else:
        power_cord[i] += list(range(a, b-1, -1))
# [[1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9], [2], [4, 3, 2, 1], [6, 5, 4], [10], [9, 8, 7], [7, 6]]

cut = 0
while True:
    cut_or_not = []
    if len(power_cord) < 2:
        break
    for i in range(len(power_cord)):
        temp = power_cord[i]
        cnt = 0
        for j in range(len(power_cord)):
            temp2 = power_cord[j]
            if temp2 == temp:
                pass
            else:
                if temp[0] < temp2[0] and temp[-1] < temp2[-1]:
                    pass
                elif temp[0] > temp2[0] and temp[-1] > temp2[-1]:
                    pass
                else:
                    # temp3 = list(set(temp).intersection(temp2))
                    cnt += 1
        cut_or_not.append(cnt)

    if not cut_or_not:
        break

    for i in cut_or_not:
        if max(cut_or_not) == i:
            power_cord.pop(cut_or_not.index(i))
            cut += 1
            break

print(cut)