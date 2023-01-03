a, d, n = map(int, input().split())
m = max([a,d,n])
for i in range(1, a*d*n+1):
    if m*i % a == 0 and m*i % d == 0:
        print(m*i)
        break