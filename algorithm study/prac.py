
def check_n(n):
    if n < 100:
        return 1
    else:
        arr=[]
        while n:
            arr.append(n%10)
            n//=10

        diff = arr[1]-arr[0]
        # print(diff)
        for i in range(2, len(arr)):
            temp = arr[i]-arr[i-1]
            if temp != diff:
                return 0
        return 1

n = int(input())

cnt = 0
for i in range(1, n+1):
    if check_n(i):
        print(i)
        cnt += 1

print(cnt)
