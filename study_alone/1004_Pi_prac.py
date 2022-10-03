# 중복 순열 연습
def pi(s, n, r):
    if s == r:
        print(p)
    else:
        for i in range(n):
            p[s] = arr[i]
            pi(s+1, n, r)

arr = [1,2,3]
n = len(arr)
r = 2
p = [0]*r
pi(0, n, r)