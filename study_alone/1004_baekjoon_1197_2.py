# 최소 스패닝 트리
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

from sys import stdin
V, E = map(int, stdin.readline().split())
edges = []
for _ in range(E):
    s, e, w = map(int, stdin.readline().split())
    edges.append([s,e,w])
edges.sort(key=lambda x:x[2])
rep = list(range(V+1))

cnt = 0
total = 0
for si, sj, sw in edges:
    if find_set(si) != find_set(sj):    # 사이클을 만들지 않는다면
        union(si, sj)                   # si를 대표원소로 해서 묶고
        total += sw                     # 가중치 ++
        cnt += 1                        # MST 간선 개수는 V-1.
        if cnt == V-1:                  # 도달하면 종료
            break

# print(sum(mst[1:]))
print(total)
