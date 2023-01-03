# 경쟁적 전염
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S,X,Y = map(int, input().split())
X,Y = X-1,Y-1
delta = [[0,1],[1,0],[0,-1],[-1,0]]

viruses = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            viruses.append((i,j,arr[i][j]))
# 번호가 낮은 놈부터 증식하는 조건을 만족시키위해 sort
viruses.sort(key=lambda x:x[2])

# 반복문 1. 시간조건 : t초에서 S초가 되면 종료
t=0
while t!=S:

   # 반복문 2. 바이러스 증식 : 낮은번호부터 증식하는데,
   for _ in range(len(viruses)):
        x,y,virus = viruses.pop(0)
        for di,dj in delta:
            ni,nj=x+di,y+dj
            if 0<=ni<N and 0<=nj<N and not arr[ni][nj]:
                arr[ni][nj]=virus
                viruses.append((ni,nj,virus))

                # 2-1. 만약 (X,Y)에 증식했다면 더 볼 것없이 종료
                if (ni,nj)==(X,Y):
                    print(virus)
                    exit(0)

   t += 1
print(arr[X][Y])