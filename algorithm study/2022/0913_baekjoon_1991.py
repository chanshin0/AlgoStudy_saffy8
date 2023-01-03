# 트리 순회
def preorder(s):
    if s in par[1:]:
        print(s, end='')
        preorder(chL[par.index(s)])
        preorder(chR[par.index(s)])
def inorder(s):
    if s in par[1:]:
        inorder(chL[par.index(s)])
        print(s, end='')
        inorder(chR[par.index(s)])
def pstorder(s):
    if s in par[1:]:
        pstorder(chL[par.index(s)])
        pstorder(chR[par.index(s)])
        print(s, end='')

N = int(input())
par = [0]*(N+1)
chL = [0]*(N+1)
chR = [0]*(N+1)

for i in range(N):
    arr = list(input().split())
    par[i+1] = arr[0]
    if arr[1] != '.':
        chL[i+1] = arr[1]
    if arr[2] != '.':
        chR[i+1] = arr[2]

# print(par)
# print(chL)
# print(chR)
preorder('A')
print()
inorder('A')
print()
pstorder('A')