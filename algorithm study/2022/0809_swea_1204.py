T = int(input())
# T =1
for j in range(1, T+1):
    j = int(input())
    s = list(map(int, input().split()))
    set_s = set(s)
    cnt = {}
    for i in set_s:
        cnt.setdefault(i, s.count(i))
    sorted_cnt = sorted(cnt.items(), key=lambda x : (x[1], x[0]))   
    modeV = sorted_cnt[-1][0]

    print(f'#{j} {modeV}')

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 