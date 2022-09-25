# 로또
def nCr(n, r, s):
    if r == 0:

        print(*comb[::-1])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = arr[i]
            nCr(n, r-1, i+1)


while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    k = arr[0]
    arr = arr[1:]
    n = len(arr)
    r = 6
    comb = [0]*r
    nCr(n, r, 0)
    print()
