N = int(input())
lst = []
sum_lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
# print(lst)
for i, j in enumerate(lst):
    sum_lst.append(j[i+1]+)