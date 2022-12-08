# 개똥벌레
N, H = map(int, input().split())
area = [[0]*N for _ in range(H)]
for n in range(N):
    obstacle = int(input())
    if n%2:
        for i in range(obstacle):
            area[i][n] = 1
    else:
        for i in range(H-1,H-obstacle-1, -1):
            area[i][n] = 1

# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
# [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
# [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

rst = list(map(sum, area))
print(min(rst), rst.count(min(rst)))
