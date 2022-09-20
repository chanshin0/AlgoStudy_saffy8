# 알고리즘 수업 - 피보나치 수 1
def fibo(n):
    global cnt1
    if n == 1:
        cnt1 = n
    elif n == 2:
        cnt1 = n
    else:
        cnt1 += 1
        return fibo(n-1) + fibo(n-2)

def fibo2(n):
    global cnt2
    f = [1]*(n+1)
    if n == 1:
        cnt2 = n
        return 1
    elif n == 2:
        cnt2 = n
        return 1
    else:
        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2]
            cnt2 += 1
    return f[n]

T = int(input())
cnt1 = 2
cnt2 = 2
fibo(T)
fibo2(T)
print(cnt1, cnt2)