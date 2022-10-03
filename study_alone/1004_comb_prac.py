# 조합 연습
def combination(s, n, r):   # s: 조합을 선택할 arr의 시작인덱스.
    if r == 0:
        print(comb[::-1])
    else:
        for i in range(s, n-r+1):   # 맨왼쪽은 s, 맨 오른쪽 n에서 최소 r개 선택할 만큼 남겨두고..
            comb[r-1] = arr[i]
            combination(i+1, n, r-1)

arr = [1,2,3,4,5]
n = len(arr)
r = 3
comb = [0]*r
combination(0, n, r)