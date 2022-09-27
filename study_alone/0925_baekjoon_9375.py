# 패션왕 신해빈

T = int(input())
for tc in range(T):
    n = int(input())

    clothes = dict()
    for i in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    # [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']]

    cnt = 1
    for t in clothes.keys():
        cnt *= (clothes[t]+1)

    print(cnt-1)