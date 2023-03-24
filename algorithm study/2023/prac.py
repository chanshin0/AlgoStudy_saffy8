# 하늘에서 별똥별이 빗발친다
N,M,L,K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]
blocked_star = 0

def tram(x,y):
    global blocked_star
    cnt = 0
    for i in range(x,x+L+1):
        for j in range(y,y+L+1):
            if [i,j] in stars:
                cnt += 1
            maximum = (x+L-i)*(y+L-j)
            if cnt+maximum < blocked_star:
                return
    blocked_star = max(blocked_star, cnt)
    return

for x, y in stars:
    tram(x,y)
print(blocked_star)