# 숫자판 점프
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i, j, num):
    num += str(arr[i][j])
    for di, dj in delta:
        ni = i+di
        nj = j+dj
        if 0 <= ni < 5 and 0 <= nj < 5 and len(num) < 6:
            dfs(ni, nj, num)
        if len(num) == 6:
            if num not in mydigit:
                mydigit.append(num)


arr = [list(map(int, input().split())) for _ in range(5)]

mydigit = []
delta = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(mydigit))



