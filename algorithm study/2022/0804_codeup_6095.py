location =[[0 for i in range(19)] for j in range(19)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    location[x][y] = 1

for i in location:
    for j in i:
        print(j, end=' ')
    print()