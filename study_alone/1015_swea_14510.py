# 나무 높이
'''
5
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    boss = max(trees)

    babies = []
    for i in trees:
        if i != boss:
            babies.append(boss-i)
    # print(babies)

    days = 1
    if babies:
        while babies:
            s = babies.pop(0)
            if s == 2:
                if days%2 == 0:
                    days += 1
                else:
                    babies.append(s)
                    if babies.count(s) == len(babies):
                        days += 2*len(babies)
                        break
            elif s == 1:
                if days%2 == 1:
                    days += 1
                else:
                    babies.append(s)
                    if babies.count(s) == len(babies):
                        days += 2*len(babies)
                        break
            else:
                if days % 2 == 1:
                    babies.append(s - 1)
                else:
                    babies.append(s - 2)
                days += 1

        print(days-1)
    else:
        print(0)
