# 숨바꼭질2
from collections import deque
N, K = map(int, input().split())

if N == K:                                  # [반례] N==K일 경우
    print(0)
    print(1)
    exit(0)

INF = 100000
visited = [INF]*(INF+1)                     # 유효범위는 0<=R<=100000, 각 요소를 INF값으로 초기화
walk = [1,-1]
teleport = [2]

def bfs(i):
    visited[i] = 0                          # 출발지점 0으로 설정.
    que = deque([i])
    cnt = 0                                 # 가짓수 카운트
    while que:
        now = que.popleft()
        if now == K:                        # K에 도착하면 종료
            return visited[now], cnt

        for w in walk:
            next = now+w
                                            # [진입조건1] next가 범위 내에 있고, 최소시간이 갱신될때에 진입
            if 0 <= next <= INF and visited[next] > visited[now]:
                visited[next] = visited[now] + 1
                que.append(next)
                if next == K:               # bfs니까 진입조건1에서 진입했으면, next==K일때 카운트하면 된다.
                    cnt += 1

        # 여기는 순간이동할 때, 로직은 위와 같음.
        for t in teleport:
            next = t*now
            if 0 <= next <= INF and visited[next] > visited[now]:
                visited[next] = visited[now] + 1
                que.append(next)
                if next == K:
                    cnt += 1

ans = bfs(N)
for a in ans:
    print(a)