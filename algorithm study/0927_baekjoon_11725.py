# 트리의 부모 찾기
N = int(input())
tree = [[] for _ in range(N+1)]

for n in range(N-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

parents = [0]*(N+1)             # 부모지정 + visited 역할하는 리스트
que = [1]                       # 큐 생성 후 루트 인큐
while que:
    top = que.pop(0)        
    child = tree[top]
    for c in child:             # 트리에 담긴 자식들을 순회하면서
        if not parents[c]:      # 아직 부모가 안정해진 애들이면
            parents[c] = top    # top을 부모로 지정하고
            que.append(c)       # 인큐

print('\n'.join(map(str, parents[2:])))

