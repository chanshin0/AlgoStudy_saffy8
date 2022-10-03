# 베이비진, 순열
def npr(n, k):
    global ans
    if n == k:
        runn = 0
        tri = 0
        if p[0] == p[1] and p[1] == p[2]:
            tri += 1
        if p[3] + 1 == p[4] and p[4]+1 == p[5]:
            runn += 1
        if runn + tri == 2:
            ans = 1
    else:
        for i in range(k):      # 모든 원소에 대해
            if not used[i]:     # 아직 사용되지 않았다면
                p[n] = nums[i]  # 순열에 넣고
                used[i] = 1     # 사용처리 후
                npr(n+1, k)     # 다음 자리 정하러 보냄
                used[i] = 0     # 초기화
T = int(input())
for tc in range(T):
    nums = list(map(int, input()))
    l = 6
    p = [0]*l
    used = [0]*l
    ans = 0
    npr(0, l)

    print(f'#{tc+1} Baby Gin') if ans else print(f'#{tc+1} Lose')
