# 이중 우선순위 큐 # 얼론

T = int(input())
for tc in range(1,T+1):
    k = int(input())
    que = []
    for _ in range(k):
        com, n = input().split()
        n = int(n)
        if com == "I":
            que.append(n)
        else:
            if not que:
                continue
            else:
                if n == -1:
                    que.remove(min(que))
                else:
                    que.remove(max(que))
    
    print(max(que), min(que)) if que else print("EMPTY")
    