N = int(input())
n_lst = []
for i in range(N):
    s = list(map(int, input().split()))
    for j in s:
        n_lst.append(j)
    n_lst.sort(reverse=True)
    n_lst = n_lst[:N]
print(sorted(n_lst)[-N])

## 모든 수가 자신의 한 칸 위에 있는 수보다 크다는 것은
## 문제의 조건이라서 생각할 필요 없다고 생각했음..