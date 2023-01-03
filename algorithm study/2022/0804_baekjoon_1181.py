n = int(input())

lst = [input() for i in range(n)]

lst.sort(key = lambda x : (len(x), x))
for i in range(len(lst)-1):
    if lst[i] != lst[i+1]:
        print(lst[i])
print(lst[len(lst)-1])