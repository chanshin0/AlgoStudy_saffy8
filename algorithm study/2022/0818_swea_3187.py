# 양치기 꿍
R, C = map(int, input().split())
arr = [input() for _ in range(R)]

lamb = 0
wolf = 0
fence = []
for i in range(R): # R줄
    for j in range(C): # C개
        if arr[i][j] == '#':
            fence.append([i, j])
#print(fence)
