# 수 정렬하기 2
N = int(input())
lst = [0]*(N)
for i in range(N):
    lst[i] = int(input())
lst.sort()
print('\n'.join(map(str, lst)))