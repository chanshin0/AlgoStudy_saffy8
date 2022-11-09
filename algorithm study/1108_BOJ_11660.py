# 구간 합 구하기 5
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
area = [[0]+list(map(int, input().split())) for _ in range(N)]
culcumative_area = [[0]*(N+1) for _ in range(N)]

for i in range(N):
    for j in range(1, N+1):
        culcumative_area[i][j] = culcumative_area[i][j-1]+area[i][j]
# [[0, 1, 3, 6, 10], [0, 2, 5, 9, 14], [0, 3, 7, 12, 18], [0, 4, 9, 15, 22]]

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())

    ans = 0
    for x in range(x1-1, x2):
        ans += culcumative_area[x][y2]-culcumative_area[x][y1-1]
    print(ans)
'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
'''