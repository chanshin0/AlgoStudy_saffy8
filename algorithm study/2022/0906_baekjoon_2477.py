# 참외밭
import sys
K = int(sys.stdin.readline())
direction = []
length = []
for i in range(6):
    d, l = map(int, sys.stdin.readline().split())
    direction.append(d)
    length.append(l)
# [4, 2, 3, 1, 3, 1]
# [50, 160, 30, 60, 20, 100]

width = 0
height = 0
width_idx = 0
height_idx = 0

for i in range(6):
    if direction[i] == 1 or direction[i] == 2: # 동서
        if length[i] > width:
            width = length[i]
            width_idx = i
    else:                                      # 남북
        if length[i] > height:
            height = length[i]
            height_idx = i

temp_w = 0
temp_h = 0
if (width_idx - 1)%6 == (height_idx)%6:
    temp_h = height - length[(width_idx + 1)%6]
    temp_w = width - length[(height_idx - 1)%6]
else:
    temp_h = height - length[(width_idx - 1)%6]
    temp_w = width - length[(height_idx + 1)%6]

chame = (width*height) - (temp_w*temp_h)
print(chame*K)