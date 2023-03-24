# 하늘에서 별똥별이 빗발친다
N,M,L,K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]
stars.sort(key=lambda x:(x[0],x[1]))
blocked_star = 0
# [[2, 4], [3, 1], [4, 7], [5, 6], [7, 3], [8, 6], [12, 10]]

for x, y in stars:
    # tempArr = stars.map((star)=>star[0]<=x+L)
    compareArr = [star for star in stars if x <= star[0] <= x+L]
    cnt = len(compareArr)
    if cnt < blocked_star: break
    for i in range(len(compareArr)):
        for j in range(i+1, len(compareArr)):
            diff = abs(compareArr[i][1] - compareArr[j][1])
            if diff > L:
                cnt -= 1
    blocked_star = max(blocked_star, cnt)
print(K-blocked_star)