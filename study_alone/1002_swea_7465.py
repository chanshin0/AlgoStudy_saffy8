# 창용 마을 무리의 개수
def find_set(x):
    while x != relations[x]:
        x = relations[x]
    return x

def union(x, y):
    relations[find_set(y)] = find_set(x)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    relations = list(range(N+1))
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    ans = set()
    for i in relations[1:]:
        ans.add(find_set(i))

    print(f'#{tc+1} {len(ans)}')