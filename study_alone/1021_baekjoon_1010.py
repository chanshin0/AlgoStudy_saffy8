# 다리 놓기
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

def f_dp(n):
    dp = [0]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    ans = f_dp(M)//f_dp(M-N)//f_dp(N)
    print(ans)