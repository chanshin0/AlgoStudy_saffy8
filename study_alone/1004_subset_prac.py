# 부분집합 연습
def f(i, k):
    if i == k:
        print(bit)
    else:
        f(i+1, k)       # i번째 비트를 0으로 정하고 다음 인덱스 정하러 보냄
        bit[i] = 1
        f(i+1, k)       # i번째 비트를 1로 정하고 다음 인덱스 정하러 보냄

arr = [1,2,3]
n = len(arr)
bit = [0]*n
f(0, n)