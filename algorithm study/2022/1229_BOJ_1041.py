# 주사위

N = int(input())
sides = list(map(int, input().split()))
cnt_sides = [N**3]*6
row = N
col = N-1

bot_idx = sides.index(max(sides))
while row:
    cnt_sides[bot_idx] -= N**2
    row -=1

print(cnt_sides)

col_max = 0
for i in range(6):
    if cnt_sides[i] and i+bot_idx != 5:
       if sides[i] > col_max:





