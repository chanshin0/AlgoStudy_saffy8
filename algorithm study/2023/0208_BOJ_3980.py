# 선발명단
C = int(input())
for tc in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    # print(arr)
    starting = [0]*11
    myMax = [0]*11
    for i in range(11):
        for j in range(11):
            if arr[i][j] and myMax[i] < arr[i][j]:
                starting[i] = i
                myMax[i] = arr[i][j]
    print(starting)
    print(myMax)
    print(sum(myMax))