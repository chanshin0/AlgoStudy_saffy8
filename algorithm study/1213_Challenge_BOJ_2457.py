# 공주님의 정원
from collections import deque

N = int(input())
flowers = []
for _ in range(N):
    # m1, d1, m2, d2 = map(int, input().split())
    flowers.append(list(map(int, input().split())))

flowers.sort(key=lambda x:(x[0],x[1]))
print(flowers)

que = deque(flowers)

start = []
end = []

while que:
    m1,d1,m2,d2 = que.popleft()
