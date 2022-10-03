# 일곱 난쟁이
# 9개 중에 7개 뽑기 (조합)
# 조합 이거 아닌데 어쩃든 답은 맞추는 풀이..
# 조합 구현 잘못된것임!
def combination(s, n, r):   # 이번에 정하는 index자리, n개 중 r개 뽑는 조합
    if s == r:
        # print(comb)
        if sum(comb) == 100:
            comb.sort()
            for i in range(r):
                print(comb[i])
            exit(0)
    else:
        for i in range(s, n):              # 모든 원소에 대해서
            if not used[i]:             # 사용되지 않은 원소라면
                comb[s] = heights[i]    # 조합에 사용
                used[i] = 1             # 사용 표시
                combination(s+1, n, r)  # 다음 자리 구하러 보냄
                used[i] = 0

heights = [0]*9
l = 9
r = 7
for i in range(9):
    heights[i] = int(input())

comb = [0]*r
used = [0]*l
combination(0, l, r)