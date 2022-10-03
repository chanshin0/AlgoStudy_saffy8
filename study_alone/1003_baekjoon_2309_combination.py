# 일곱 난쟁이
# 9개 중에 7개 뽑기 (조합)
def combination(s, n, r):
    if r == 0:
        # print(comb[::-1])
        if sum(comb) == 100:
            comb.sort()
            print('\n'.join(map(str, comb)))
            exit(0)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = heights[i]      # 맨뒷칸부터 채움. comb의 r-1정하고,
            combination(i+1, n, r-1)    # i+1~에서 r-1개 뽑는 조합 돌려라
            # 그니까 예를 들어 10개에서 3개 뽑는 경우일 때
            # 한자리 정하고 9개에서 2개 뽑,
            # 다시 8개에서 1개 뽑는 식으로 정하는 것

heights = [0]*9
l = 9
r = 7
for i in range(9):
    heights[i] = int(input())

comb = [0]*r
combination(0, l, r)