# K번째 수

N = int(input())
K = int(input())

for n in range(1, N**2+1):
    for i in range(1, N+1):
        if n%i == 0 and n//i <= N:
            K -= 1


    if K <= 0:
        print(n)
        break
    # print(n, K)

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# 1 2 3 4 5 6 7 8 9 0 1 2 3 4   5  6
# 1 2 2 3 3 4 6 6 9
# 1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16