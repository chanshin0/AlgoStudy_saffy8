# 순열 연습
def pi(s, n, r):
    if s == r:
        print(p)
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                p[s] = arr[i]
                pi(s+1, n, r)
                used[i] = 0

arr = [1,2,3]
n = len(arr)
r = 2
p = [0]*r
used = [0]*n
pi(0, n, r)